#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <assert.h>
#include <string.h>

#include <netinet/in.h>
#include <arpa/inet.h>

void error(char *msg) {
  perror(msg);
  exit(1);
}

int main( int argc, char *argv[] ) {
    int sockfd; /* server socket */
    int newsockfd; /* client socket */
    int portno; /* port to listen on */
    int clilen; /* byte size of client's address */
    int n; /* message byte size */
    struct sockaddr_in serv_addr; /* server's addr */
    struct sockaddr_in cli_addr; /* client addr */
    char buffer[256]; /* message buffer */
    char *hostaddrp; /* dotted decimal host addr string of client */

    if (argc < 2) {
        fprintf(stderr,"usage %s port\n", argv[0]);
        exit(0);
    }

    portno = atoi(argv[1]);
    
    /* step 1. Create a socket with the socket() system call */
    // sockfd = socket(int socket_family, int socket_type, int protocol);
    // family − It specifies the protocol family
    //    +----------+-----------------------+
    //    |  Family  |      Description      |
    //    +----------+-----------------------+
    //    | AF_INET  | IPv4 protocols        |
    //    | AF_INET6 | IPv6 protocols        |
    //    | AF_LOCAL | Unix domain protocols |
    //    | ...      |                       |
    //    +----------+-----------------------+
    // type − It specifies the kind of socket you want
    //    +-------------+-----------------+
    //    |    Type     |   Description   |
    //    +-------------+-----------------+
    //    | SOCK_STREAM | Stream socket   |
    //    | SOCK_DGRAM  | Datagram socket |
    //    | ...         |                 |
    //    +-------------+-----------------+
    // protocol − specifies the low-level mechanism to transmit and receive data.
    // Each protocol is valid for a particular namespace-style combination.
    //    +-------------+------------------------+
    //    |  Protocol   |      Description       |
    //    +-------------+------------------------+
    //    | IPPROTO_TCP | TCP transport protocol |
    //    | IPPROTO_UDP | UDP transport protocol |
    //    | ...         |                        |
    //    +-------------+------------------------+
    // If socket succeeds, it returns a file descriptor for the socket.
    // You can read from or write to the socket using read, write.
    // When you are finished with a socket, call close to remove it.
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    
    if (sockfd < 0)
        error("ERROR opening socket");
    // #include <netinet/in.h>
    // struct sockaddr
    // {
    //     unsigned short sa_family;  /* Address family (e.g., AF_INET)  */
    //     char sa_data[14];          /* Protocol-specific address information */
    // };
    // struct sockaddr_in {
    //     sa_family_t    sin_family; /* address family: AF_INET */
    //     in_port_t      sin_port;   /* port in network byte order */
    //     struct in_addr sin_addr;   /* internet address */
    // };
    /* Internet address. */
    // struct in_addr {
    //     uint32_t       s_addr;     /* address in network byte order */
    // };
    /* Initialize address structure */
    bzero((char *) &serv_addr, sizeof(serv_addr));    
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);
    
    /* step 2. Bind the socket to an address using the bind() system call */
    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
        error("ERROR on binding");
    
    /* step 3. Listen for connections with the listen() system call */
    if (listen(sockfd,5) < 0)
        error("ERROR on listening");
    
    clilen = sizeof(cli_addr);
    /* step 4. Accept a connection with the accept() system call. This call typically blocks until a client connects with the server */
    // http://man7.org/linux/man-pages/man2/accept.2.html
    newsockfd = accept(sockfd, (struct sockaddr *)&cli_addr, &clilen);

    if (newsockfd < 0)
        error("ERROR on accept");
    
    // char *inet_ntoa(struct in_addr in);
    // The inet_ntoa() function converts the Internet host address in, 
    // given in network byte order, to a string in IPv4 dotted-decimal notation.
    hostaddrp = inet_ntoa(cli_addr.sin_addr);
    if (hostaddrp == NULL)
        error("ERROR on inet_ntoa\n");
    printf("Connected with %s\n", hostaddrp);

    /* step 5. Send and receive data using the read() and write() system calls */
    bzero(buffer, 256);
    n = recv(newsockfd, buffer, 255, 0);
    
    if (n < 0)
        error("ERROR reading from socket");
    assert(buffer[n-1]=='\n');
    assert(buffer[n]=='\0');
    printf("Received %d bytes from client: %s\n", n, buffer);
    
    /* Write a response to the client */
    n = write(newsockfd, buffer, strlen(buffer));
    
    if (n < 0)
        error("ERROR writing to socket");

    close(sockfd);

    return 0;
}