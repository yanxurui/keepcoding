#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <assert.h>
#include <string.h>

#include <netinet/in.h>
#include <arpa/inet.h>

#include <sys/wait.h>

void error(char *msg)
{
  perror(msg);
  exit(1);
}

int main( int argc, char *argv[] )
{
    int sockfd; /* server socket */
    int newsockfd; /* client socket */
    int portno; /* port to listen on */
    int clilen; /* byte size of client's address */
    int n; /* message byte size */
    struct sockaddr_in serv_addr; /* server's addr */
    struct sockaddr_in cli_addr; /* client addr */
    char buffer[256]; /* message buffer */

    if (argc < 2) {
        fprintf(stderr,"usage %s port\n", argv[0]);
        exit(0);
    }

    portno = atoi(argv[1]);

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    
    if (sockfd < 0)
        error("ERROR opening socket");

    bzero((char *) &serv_addr, sizeof(serv_addr));    
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);
    
    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
        error("ERROR on binding");
    
    if (listen(sockfd,5) < 0)
        error("ERROR on listening");
    
    clilen = sizeof(cli_addr);

    int pid = getpid();
    printf("parent process %d\n", pid);

    for (int i = 0; i < 2; i++)
    {
        pid = fork();
        if (pid < 0)
        {
            error("failed to fork");
        }
        else if (pid==0) // child
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

    while(1)
    {
        newsockfd = accept(sockfd, (struct sockaddr *)&cli_addr, &clilen);
        if (newsockfd < 0)
            error("ERROR on accept");

        printf("process %d get connection %d\n", getpid(), newsockfd);

        bzero(buffer, 256);
        n = recv(newsockfd, buffer, 255, 0);
        if (n < 0)
            error("ERROR reading from socket");
        if (n >0 ) // n==0 means client close connection
        {
            n = write(newsockfd, buffer, strlen(buffer));
            if (n < 0)
                error("ERROR writing to socket");
        }   
        close(newsockfd);
    }

    return 0;
}