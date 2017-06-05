#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <netdb.h>
#include <netinet/in.h>
#include <ev.h>

#define BUFFER_SIZE 1024

char buffer[BUFFER_SIZE] = "";
int sd;

void stdin_cb(struct ev_loop *loop, ev_io *w, int revents);
void recv_cb(EV_P_ ev_io *w, int revents);

int main(int argc, char *argv[])
{
    struct ev_loop *loop = EV_DEFAULT;
    struct sockaddr_in addr;
    ev_io stdin_watcher, recv_watcher;

    if (argc < 3) {
        fprintf(stderr,"usage %s hostname port\n", argv[0]);
        exit(0);
    }

    // Create client socket
    if( (sd = socket(PF_INET, SOCK_STREAM, 0)) < 0 )
    {
        perror("socket error");
        return -1;
    }

    bzero(&addr, sizeof(addr));

    struct hostent *server = gethostbyname(argv[1]);
    if (server == NULL) {
        perror("ERROR, no such host\n");
        return -1;
    }
    
    addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, (char *)&addr.sin_addr.s_addr, server->h_length);
    addr.sin_port = htons(atoi(argv[2]));


    // Connect to server socket
    if(connect(sd, (struct sockaddr *)&addr, sizeof addr) < 0)
    {
        perror("Connect error");
        return -1;
    }
    printf("connected successfully!\n");

    ev_io_init(&stdin_watcher, stdin_cb, /*STDIN_FILENO*/ 0, EV_READ);
    ev_io_start(loop, &stdin_watcher);

    ev_io_init(&recv_watcher, recv_cb, sd, EV_READ);
    ev_io_start(loop, &recv_watcher);
    
    // It will ask the operating system for any new events, 
    // call the watcher callbacks, and then repeat the whole process indefinitely
    ev_run(loop, 0);

    return 0;
}
// Read input from user and send message to the server
void stdin_cb(struct ev_loop *loop, ev_io *w, int revents)
{
    fgets(buffer, sizeof(buffer), stdin);
    if(strcmp(buffer, "quit\n") == 0) {
        // this causes all nested ev_run's to stop iterating
        ev_break (EV_A_ EVBREAK_ALL);
        close(sd);
    }
    else {
        send(sd, buffer, strlen(buffer), 0);
    }
    
}

// Receive message from the server
void recv_cb(EV_P_ ev_io *w, int revents)
{
    ssize_t read;
    if(EV_ERROR & revents)
    {
        perror("got invalid event");
        return;
    }

    read = recv(w->fd, buffer, BUFFER_SIZE, 0);
    if(read < 0)
    {
        perror("read error");
    }
    else if(read == 0)
    {
        // it will result in dead loop if we don't stop ev loop
        ev_break (EV_A_ EVBREAK_ALL);
        close(sd);
        perror("server might close");
    }
    else {
        printf(buffer);
    }
}




