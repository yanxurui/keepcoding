#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <netdb.h>
#include <netinet/in.h>

#include <string.h>

void error(char *msg) {
  perror(msg);
  exit(1);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, n;
    struct sockaddr_in serv_addr;
    struct hostent *server;

    char buffer[256];
    
    if (argc < 3) {
        fprintf(stderr,"usage %s hostname port\n", argv[0]);
        exit(0);
    }
    
    portno = atoi(argv[2]);
    
    /* step 1. Create a socket with the socket() system call */
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        error("ERROR opening socket");
    }
    
    // #include <netdb.h>
    // struct hostent *gethostbyname(const char *name);

    // The hostent structure is defined in <netdb.h> as follows:
    // struct hostent {
    //     char  *h_name;             official name of host 
    //     char **h_aliases;         /* alias list */
    //     int    h_addrtype;        /* host address type */
    //     int    h_length;          /* length of address */
    //     char **h_addr_list;       /* list of addresses */
    // }
    // #define h_addr h_addr_list[0] /* for backward compatibility */
    server = gethostbyname(argv[1]);
    
    if (server == NULL) {
        error("ERROR, no such host\n");
    }
    
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, (char *)&serv_addr.sin_addr.s_addr, server->h_length);
    serv_addr.sin_port = htons(portno);
    
    /* step 2. Connect the socket to the address of the server using the connect() system call */
    if (connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
        error("ERROR connecting");
    }
    
    /* Now ask for a message from the user, this message
        * will be read by server
    */
    
    printf("Please enter the message: ");
    bzero(buffer,256);
    fgets(buffer,255,stdin);
    
    /* step 3. Send and receive data */
    /* Send message to the server */
    n = write(sockfd, buffer, strlen(buffer));
    
    if (n < 0) {
        error("ERROR writing to socket");
    }
    
    /* Now read server response */
    bzero(buffer,256);
    n = read(sockfd, buffer, 255);
    
    if (n < 0) {
        error("ERROR reading from socket");
    }
    
    printf("Echo from server: %s\n", buffer);

    close(sockfd);

    return 0;
}