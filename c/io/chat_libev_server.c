#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <netinet/in.h>
#include <arpa/inet.h>
#include <ev.h>

#include <assert.h>

#define BUFFER_SIZE 1024
#define MAX_CLIENT 1000

int online_clients = 0;  // Total number of connected clients
char* clients[MAX_CLIENT] = {NULL};

void accept_cb(struct ev_loop *loop, struct ev_io *watcher, int revents);
void read_cb(struct ev_loop *loop, struct ev_io *watcher, int revents);

int main(int argc, char *argv[])
{
    struct ev_loop *loop = ev_default_loop(0);
    int sd;
    struct sockaddr_in addr;
    int addr_len = sizeof(addr);
    struct ev_io w_accept;

    if (argc < 2) {
        fprintf(stderr,"usage %s port\n", argv[0]);
        exit(0);
    }

    // Create server socket
    if( (sd = socket(PF_INET, SOCK_STREAM, 0)) < 0 )
    {
        perror("socket error");
        return -1;
    }

    /* 
    * setsockopt: Handy debugging trick that lets
    * us rerun the server immediately after we kill it; 
    * otherwise we have to wait about 20 secs. 
    * Eliminates "ERROR on binding: Address already in use" error. 
    * The SO_REUSEADDR is for when the socket bound to an address has already been closed,
    * the same address (ip-address/port pair) can be used again directly. 
    */
    int optval = 1;
    setsockopt(sd, SOL_SOCKET, SO_REUSEADDR, 
         (const void *)&optval , sizeof(int));

    bzero(&addr, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(atoi(argv[1]));
    addr.sin_addr.s_addr = INADDR_ANY;

    // Bind socket to address
    if (bind(sd, (struct sockaddr*) &addr, sizeof(addr)) != 0)
    {
        perror("bind error");
        return -1;
    }

    // Start listing on the socket
    if (listen(sd, 2) < 0)
    {
        perror("listen error");
        return -1;
    }

    // Initialize and start a watcher to accepts client requests
    ev_io_init(&w_accept, accept_cb, sd, EV_READ);
    ev_io_start(loop, &w_accept);

    // Start loop
    ev_run(loop, 0);

    return 0;
}

/* Accept client requests */
void accept_cb(struct ev_loop *loop, struct ev_io *watcher, int revents)
{
    struct sockaddr_in client_addr;
    socklen_t client_len = sizeof(client_addr);
    int client_sd;
    struct ev_io *w_client = (struct ev_io*) malloc (sizeof(struct ev_io));

    if(EV_ERROR & revents)
    {
        perror("got invalid event");
        return;
    }

    // Accept client request
    client_sd = accept(watcher->fd, (struct sockaddr *)&client_addr, &client_len);

    if (client_sd < 0)
    {
        perror("accept error");
        return;
    }
    if (client_sd >= MAX_CLIENT)
    {
        perror("too many clients");
        close(client_sd);
        return;
    }
    // accept would return unused file descriptor monotonically
    // fd is guaranteed to be unique
    clients[client_sd] = (char *)malloc(sizeof(char)*30);
    sprintf(clients[client_sd], "%s:%d", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));
    printf("Connected with %s\n", clients[client_sd]);
    online_clients ++; // Increment online_clients count
    printf("%d client(s) online.\n", online_clients);

    // Initialize and start watcher to read client requests
    ev_io_init(w_client, read_cb, client_sd, EV_READ);
    ev_io_start(loop, w_client);
}

/* Read client message */
void read_cb(struct ev_loop *loop, struct ev_io *watcher, int revents){
    char buffer[BUFFER_SIZE];
    int client_sd = watcher->fd;
    ssize_t read;

    if(EV_ERROR & revents)
    {
        perror("got invalid event");
        return;
    }

    // Receive message from client socket
    read = recv(client_sd, buffer, BUFFER_SIZE, 0);

    if(read < 0)
    {
        perror("read error");
        return;
    }

    if(read == 0)
    {
        // Stop and free watcher if client socket is closing
        ev_io_stop(loop, watcher);
        close(watcher->fd);
        free(watcher);
        perror("peer might close");
        clients[client_sd] = NULL;
        online_clients --; // Decrement online_clients count
        printf("%d client(s) online.\n", online_clients);
        return;
    }
    
    // override newline and append client info
    sprintf(buffer+read-1, "(%s)\n", clients[client_sd]);
    // Send message to all other clients
    for(int i=0,j=0; i<online_clients;i++) {
        // j is a client socket except me
        while(clients[j] == NULL) j++;
        if(j != client_sd) {
            send(j, buffer, strlen(buffer), 0);
        }
        j++;
    }
    printf("message: %s", buffer);

    bzero(buffer, BUFFER_SIZE);
}