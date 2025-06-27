import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 63000))  
print("Serveur en attente de connexion sur le port 63000...")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec : {client_address}")
    while True:
        client_message = client_socket.recv(1024).decode()
        if not client_message:
            print("Connexion interrompue par le client.")
            break
        print(f"Client : {client_message}")
        if client_message.lower() == 'fini':
            print("Fin de la conversation avec le client.")
            break

        server_message = input("Vous (serveur) : ")
        client_socket.send(server_message.encode())

        if server_message.lower() == 'fini':
            print("Fin de la conversation avec le client.")
            break

    client_socket.close()
    print("Connexion fermée.\nEn attente d'un nouveau client...\n")
