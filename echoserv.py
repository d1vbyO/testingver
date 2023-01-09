# echo-server.py

import socket

HOST = "194.67.111.86"  # Standard loopback interface address (localhost)
PORT = 5694  # Port to listen on (non-privileged ports are > 1023)
while True:
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM,0) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
                print(data)