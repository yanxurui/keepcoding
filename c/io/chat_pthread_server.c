#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <netinet/in.h>
#include <arpa/inet.h>

#include <pthread.h>

#define BUFFER_SIZE 1024
#define MAX_CLIENT 1000

int online_clients = 0;
char* clients[MAX_CLIENT] = {NULL};

void* connection_handler(void *);

int main(int argc, char *argv[])
{
    int sd;
    struct sockaddr_in addr, client_addr;
    socklen_t client_len = sizeof(client_addr);


    if (argc < 2) {
        fprintf(stderr,"usage %s port\n", argv[0]);
        exit(0);
    }

    if( (sd = socket(PF_INET, SOCK_STREAM, 0)) < 0 )
    {
        perror("socket error");
        return -1;
    }

    bzero(&addr, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(atoi(argv[1]));
    addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(sd, (struct sockaddr*) &addr, sizeof(addr)) != 0)
    {
        perror("bind error");
        return -1;
    }

    if (listen(sd, 2) < 0)
    {
        perror("listen error");
        return -1;
    }

    while(1)
    {
        int client_sd = accept(sd, (struct sockaddr *)&client_addr, &client_len);
        if (client_sd < 0)
        {
            perror("accept error");
            return -1;
        }
        if (client_sd >= MAX_CLIENT)
        {
            perror("too many clients");
            close(client_sd);
            return -1;
        }
        clients[client_sd] = (char *)malloc(sizeof(char)*30);
        sprintf(clients[client_sd], "%s:%d", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));
        printf("Connected with %s\n", clients[client_sd]);
        online_clients++;
        printf("%d client(s) online.\n", online_clients);

        pthread_t client_thread;
        pthread_create (&client_thread, NULL, &connection_handler, &client_sd);
    }

    return 0;
}

void* connection_handler(void* socket)
{
    int client_sd = *(int*)socket;
    char buffer[BUFFER_SIZE];
    ssize_t read;

    while(1)
    {
        read = recv(client_sd, buffer, BUFFER_SIZE, 0);
        if(read < 0)
        {
            perror("read error");
            break;
        }
        if(read == 0)
        {
            perror("peer might close");
            clients[client_sd] = NULL;
            online_clients--;
            printf("%d client(s) online.\n", online_clients);
            break;
        }

        sprintf(buffer+read-1, "(%s)\n", clients[client_sd]);
        for(int i=0,j=0; i<online_clients;i++)
        {
            while(clients[j] == NULL) j++;
            if(j != client_sd) {
                send(j, buffer, strlen(buffer), 0);
            }
            j++;
        }
        printf("message: %s", buffer);

        bzero(buffer, BUFFER_SIZE);
    }
    free(buffer);
    return NULL;
}






