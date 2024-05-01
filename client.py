from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM


def message(client_socket):
    while True:
        data = client_socket.recv(2048)
        if "quit" in data.decode():
            break
        print(data.decode())
        msg = input("->")
        try:
            client_socket.sendall(msg.encode())
        except OSError:
            client_socket.close()
            break


server = ("127.0.0.1", 12345)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(server)
# Thread(target=receive, args=(client_socket,)).start()
# Thread(target=mhmessage, daemon=True).start()
message(client_socket)
