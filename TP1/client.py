import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 63000)
client_socket.connect(server_address)
message = "Serveur es-tu là ?"
client_socket.send(message.encode())
response = client_socket.recv(1024).decode()
print(f"Réponse du serveur : {response}")
client_socket.close()
print("Connexion fermee")
