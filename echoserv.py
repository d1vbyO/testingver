# echo-server.py

import binascii
import socket

Clients = []
HOST = "194.67.111.86"  # Standard loopback interface address (localhost)
PORT = 5694  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
s.bind((HOST, PORT))
s.listen()

while True:
    conn, addr = s.accept()
    print(f"Connected! {addr}")
    # Prekolist.append(conn)
    # Clients.append(conn)
    conn.send(b"You are connected to server.")
    break
while True:
    conn2,addr2 = s.accept()
    print(f"Connected! second client {addr}")
    conn2.send(b"You are connected to server too.")
    break
while True:
    while True:
        data = conn.recv(1024)

        # if not data:
        #     break
        # for g in Clients:
        print("Client 1 send to 2")
        conn2.sendall(b'Server recieved:' + data) #отправка сообщений второму клиенту
        # conn2.sendall(b'Server recieved:' + data2)
        # print(data)
        break
    while True:
        data = conn2.recv(1024)
        # data2 = conn2.recv(1024)
        # if data !=0:
        #     Clients[1].sendall(b'Server recieved:' + data)
        
        # if not data:
        #     break
        # for g in Clients:
        print("Client 2 send to 1")
        conn.sendall(b'Server recieved:' + data) #отправка сообщений второму клиенту
        # conn2.sendall(b'Server recieved:' + data2)
        # print(data)
        break


# for j in range(len(Prekolist)):
    # conn = Prekolist[j]
    


            
        # with conn:
        #     print(f"Connected by {addr}")
        #     while True:
        #         data = conn.recv(1024)
        #         if not data:
        #             break
        #         conn.sendall(data)
        #         print(data)
        #         text = input("Enter message:\n")
        #         conn.send(b'1010101')