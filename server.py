"""
Name: Syed Mahdi
Date: 8/1/2020
Course: CS 372

Sources:
1) https://realpython.com/python-sockets/
2) https://docs.python.org/3.4/howto/sockets.html
"""

import socket

HOST = "127.0.0.1"  #socket.gethostbyname(socket.gethostname())
PORT = 65432
ADDRESS = (HOST, PORT)
QUIT_MSG = "/q"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(ADDRESS)
    server.listen()
    print("Server listening on: " + HOST + " on port " + str(PORT) + "...")
    connection, address = server.accept()
    with connection:
        print("Connected by", address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
