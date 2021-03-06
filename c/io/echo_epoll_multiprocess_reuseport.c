#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <netdb.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/epoll.h>
#include <errno.h>

#define MAXEVENTS 64

void
error(char *msg)
{
    perror(msg);
    exit(1);
}

static int
create_and_bind(int port)
{
    struct sockaddr_in serv_addr;
    int s, sfd;

    sfd = socket(AF_INET, SOCK_STREAM, 0);
    
    if (sfd < 0)
    {
        perror("socket failed");
        return -1;
    }

    int optval = 1;
    setsockopt(sfd, SOL_SOCKET, SO_REUSEPORT, &optval, sizeof(optval));

    bzero((char *) &serv_addr, sizeof(serv_addr));    
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(port);
    
    if (bind(sfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
    {
        perror("bind failed");
        return -1;
    }
    return sfd;
}

static int
make_socket_non_blocking(int sfd)
{
    int flags, s;

    flags = fcntl(sfd, F_GETFL, 0);
    if (flags == -1)
    {
        perror("fcntl get");
        return -1;
    }

    flags |= O_NONBLOCK;
    s = fcntl(sfd, F_SETFL, flags);
    if (s == -1)
    {
        perror("fcntl set");
        return -1;
    }

    return 0;
}

int
main(int argc, char *argv[])
{
    int sfd, s;
    int efd;

   //  typedef union epoll_data {
   //     void        *ptr;
   //     int          fd;
   //     uint32_t     u32;
   //     uint64_t     u64;
   // } epoll_data_t;

   // struct epoll_event {
   //     uint32_t     events;      /* Epoll events */
   //     epoll_data_t data;        /* User data variable */
   // };
    struct epoll_event ep;
    struct epoll_event *eps;

    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s port\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    
    int pid = getpid();
    printf("parent process %d\n", pid);

    for(int i=0; i < 2; i++)
    {
        pid = fork();
        if (pid<0)
        {
            error("fork");
        }
        else if (pid == 0) // child
        {
            break;
        }
        else // parent
        {
            printf("start child process %d\n", pid);
        }
    }

    if (pid > 0 ) // parent
    {
        int wstatus;
        // just suspend until one child process exits
        if ((pid = wait(&wstatus)) == -1)
            error("Error on wait");
        printf("Process %d terminated\n", pid);
        return 0;
    }

    sfd = create_and_bind(atoi(argv[1]));
    if (sfd == -1)
        exit(1);

    s = make_socket_non_blocking(sfd);
    if (s == -1)
        exit(1);

    s = listen(sfd, SOMAXCONN);
    if (s == -1)
    {
        error("listen");
    }

    efd = epoll_create1(0);
    if (efd == -1)
    {
        error("epoll_create");
    }

    ep.data.fd = sfd;
    ep.events = EPOLLIN | EPOLLET;
    s = epoll_ctl(efd, EPOLL_CTL_ADD, sfd, &ep);
    if (s == -1)
    {
        error("epoll_ctl");
    }

    /* Buffer where events are returned */
    eps = calloc(MAXEVENTS, sizeof ep);

    /* The event loop */
    while (1)
    {
        int n, i;

        n = epoll_wait(efd, eps, MAXEVENTS, -1);
        for (i = 0; i < n; i++)
        {
            if ((eps[i].events & EPOLLERR) ||
                (eps[i].events & EPOLLHUP) ||
                (!(eps[i].events & EPOLLIN)))
            {
                /* An error has occured on this fd, or the socket is not
                   ready for reading (why were we notified then?) */
                if (eps[i].events & EPOLLERR)
                    fprintf(stderr, "epoll error: EPOLLERR\n");
                if (eps[i].events & EPOLLHUP)
                    fprintf(stderr, "epoll error: EPOLLHUP\n");
                close(eps[i].data.fd);
                continue;
            }
            else if (sfd == eps[i].data.fd)
            {
                /* Is is possible that more than one connections only wake up one time? 
                   https://stackoverflow.com/questions/41582560/how-does-epolls-epollexclusive-mode-interact-with-level-triggering */
                struct sockaddr in_addr;
                socklen_t in_len;
                int infd;

                in_len = sizeof in_addr;
                infd = accept(sfd, &in_addr, &in_len);
                printf("Process %d accept return %d\n", getpid(), infd);
                if (infd == -1)
                {
                    if (errno != EAGAIN || errno != EWOULDBLOCK)
                    {
                        error("accept");
                    }
                    continue;
                }

                /* Make the incoming socket non-blocking and add it to the
                   list of fds to monitor. */
                s = make_socket_non_blocking(infd);
                if (s == -1)
                    exit(1);

                ep.data.fd = infd;
                ep.events = EPOLLIN | EPOLLET;
                s = epoll_ctl(efd, EPOLL_CTL_ADD, infd, &ep);
                if (s == -1)
                {
                    error("epoll_ctl");
                }
            }
            else
            {
                /* We have data on the fd waiting to be read. Read and
                   display it. We must read whatever data is available
                   completely, as we are running in edge-triggered mode
                   and won't get a notification again for the same
                   data. */
                int done = 0;

                while (1)
                {
                    ssize_t count;
                    char buf[512];

                    count = read(eps[i].data.fd, buf, sizeof buf);
                    if (count == -1)
                    {
                        /* If errno == EAGAIN, that means we have read all
                           data. So go back to the main loop. */
                        if (errno != EAGAIN) {
                            perror("read");
                            done = 1;
                        }
                        break;
                    }
                    else if (count == 0)
                    {
                        /* End of file. The remote has closed the
                           connection. */
                        done = 1;
                        break;
                    }
                    
                    if (!strncmp(buf, "quit\n", 5))
                    {
                        done = 1;
                        break;
                    }

                    s = write(eps[i].data.fd, buf, count);
                    if (s == -1)
                    {
                        error("write");
                    }
                }

                if (done)
                {
                    // printf("Closed connection on descriptor %d\n", eps[i].data.fd);

                    /* Closing the descriptor will make epoll remove it
                       from the set of descriptors which are monitored. */
                    close(eps[i].data.fd);
                }
            }
        }
    }

    free(eps);

    close(sfd);

    return EXIT_SUCCESS;
}