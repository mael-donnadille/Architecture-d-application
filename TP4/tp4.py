import socket
import threading
import sys
import time

def connexion(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print(f"Connexion établie avec {host}:{port}")
        return s
    except Exception as e:
        print(f"Connexion impossible pour le moment : {e}")
        return None

def recevoir_message(conn):
    while True:
        try:
            message = conn.recv(1024).decode()
            if message.lower() == 'fin':
                print("L'utilisateur distant a quitté la conversation.")
                conn.close()
                sys.exit()
            print(f"Autre : {message}")
        except:
            break

def envoyer_message(conn):
    while True:
        message = input()
        try:
            conn.send(message.encode())
            if message.lower() == 'fin':
                print("Vous avez terminé la conversation.")
                conn.close()
                sys.exit()
        except:
            break

host_local = '192.168.0.100' #a modifier
port_local = 63000

host_dist = input("Entrez l'adresse IP de l'autre peer : ")
port_dist = 63000

socket_connexion = connexion(host_dist, port_dist)

if socket_connexion:
    thread_recv = threading.Thread(target=recevoir_message, args=(socket_connexion,))
    thread_send = threading.Thread(target=envoyer_message, args=(socket_connexion,))
    thread_recv.start()
    thread_send.start()
else:
    print("En attente de connexion entrante...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host_local, port_local))
    server_socket.listen(1)

    conn, addr = server_socket.accept()
    print(f"Connexion entrante depuis {addr}")

    thread_recv = threading.Thread(target=recevoir_message, args=(conn,))
    thread_send = threading.Thread(target=envoyer_message, args=(conn,))
    thread_recv.start()
    thread_send.start()
