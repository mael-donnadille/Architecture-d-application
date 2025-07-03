import socket

# Création du socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 63000) 

try:
    client_socket.connect(server_address)
    print("Connecté au serveur.")

    while True:
        client_message = input("Vous (client) : ")
        client_socket.send(client_message.encode())

        if client_message.lower() == 'fini':
            print("Fin de la conversation avec le serveur.")
            break

        server_message = client_socket.recv(1024).decode()
        print(f"Serveur : {server_message}")

        if server_message.lower() == 'fini':
            print("Le serveur a terminé la conversation.")
            break

finally:
    client_socket.close()
    print("Connexion fermée.")
