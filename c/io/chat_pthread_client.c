#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <netdb.h>
#include <netinet/in.h>
#include <pthread.h>

#define BUFFER_SIZE 1024

int sd;

void* recieve_handler(void *);

int main(int argc, char *argv[])
{
    struct sockaddr_in addr;

    if (argc < 3) {
        fprintf(stderr,"usage %s hostname port\n", argv[0]);
        exit(0);
    }

    if ((sd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
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

    if(connect(sd, (struct sockaddr *)&addr, sizeof addr) < 0)
    {
        perror("Connect error");
        return -1;
    }
    printf("connected successfully!\n");

    // receive in another thread
    pthread_t client_thread;
    pthread_create (&client_thread, NULL, &recieve_handler, NULL);

    char buffer[BUFFER_SIZE] = "";
    ssize_t write;

    // read input and send in the main thread
    while(1)
    {
        fgets(buffer, BUFFER_SIZE, stdin);
        if(strcmp(buffer, "quit\n") == 0) {
            close(sd);
            break;
        }
        else {
            write = send(sd, buffer, strlen(buffer), 0);
            if (write<0) {
                perror("send error");
                break;
            }
        }
    }
    return 0;
}

void* recieve_handler(void* arg)
{
    char buffer[BUFFER_SIZE] = "";
    ssize_t read;

    while(1)
    {
        read = recv(sd, buffer, BUFFER_SIZE, 0);
        if(read < 0)
        {
            perror("read error");
            break;
        }
        else if(read == 0)
        {
            close(sd);
            perror("read error, server might close");
        }
        else {
            printf(buffer);
            bzero(buffer, BUFFER_SIZE);
        }
    }
    exit(0); // exit the process
    return NULL;
}