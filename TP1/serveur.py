import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('', 63000)
server_socket.bind(server_address)
server_socket.listen(1)

print("Serveur en attente de connexion sur le port 63000")

client_socket, client_address = server_socket.accept()

print(f"Connexion etablie avec le client : {client_address}")

message = client_socket.recv(1024).decode()

print(f"Message recu du client : {message}")

response = message + "\nCSI present!"
client_socket.send(response.encode())
client_socket.close()
server_socket.close()
print("Connexion fermee")
