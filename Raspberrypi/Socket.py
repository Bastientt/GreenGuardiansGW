#Serv => 192.168.43.201
#Rasp => 192.168.43.21

import socket
import os

def start_server(host='192.168.43.201', port=2000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Serveur en écoute sur {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connexion acceptée de {addr}")

        with open('received_image.jpg', 'wb') as f:
            print("Réception de l'image...")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)

        print("Image reçue et sauvegardée.")
        client_socket.close()
        print(f"Connexion fermée de {addr}")

if __name__ == "__main__":
    start_server()

