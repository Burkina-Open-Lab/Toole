#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#define SERVER_PORT 42422
#define BACKLOG 16 //represente le nombre de personne qui peuvent attendre avant que le server  ne les accepts
// Hello la BOP, c'est Gérard, avec cette focntion ,je cree un socket que je vais utilisé tout dans ce fichier network.c
int create_socket(){
    int socket_tcp;
    socket_tcp=socket(AF_INET, SOCK_STREAM,0);
    if (socket_tcp<0)
        {
            perror("La création du socket server a échouer");
            return -1;
        }
    return socket_tcp;
}

// là , c'est le sever TCP  qui est chargé d'etablir la connexion avec les appareils clients
int init_server()
{
    int socket_tcp=create_socket();
    int enable=1;
    if (setsockopt(socket_tcp, SOL_SOCKET, SO_REUSEADDR,&enable, sizeof(enable))<0) {
        perror("setsockopt a echoué");
        close(socket_tcp);
        return -1;
    }
    //je definie la structure comme support de transmision
    struct sockaddr_in network_utils={
        .sin_family=AF_INET,
        .sin_port= htons(SERVER_PORT),
        .sin_addr.s_addr = htonl(INADDR_ANY)
    };

    //là j'attache le socket avec le struture network_utils de type sockaddr_in
    if (bind(socket_tcp,(struct sockaddr *)&network_utils,sizeof(network_utils))<0) {
        perror("Erreur avec bind");
        close(socket_tcp);
        return -1;
    }

    // je met le  server en mode ecoute avec listen()
    if (listen(socket_tcp, BACKLOG)<0) {
        perror("Erreur d'ecoute avec listen()");
        close(socket_tcp);
        return -1;
    }
    return socket_tcp;
}

int main()
{
    return 0;
}
