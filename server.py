"""
Name: Syed Mahdi
Date: 8/1/2020
Course: CS 372

Sources:
1) https://realpython.com/python-sockets/
2) https://docs.python.org/3.4/howto/sockets.html
"""

import socket

HOST = "localhost"
PORT = 65432
ADDRESS = (HOST, PORT)
QUIT_MSG = "/q"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(ADDRESS)
    server.listen()

    print("Server listening on: " + HOST + " on port " + str(PORT) + "...")

    connection, address = server.accept()
    connected = True

    with connection:
        print("Connected by", address)
        print("Type /q to quit\nWaiting for message...")

        while connected:
            data = connection.recv(1024)

            if not data:
                continue

            received_message = data.decode()
            if received_message == QUIT_MSG:
                connected = False
            else:
                print(received_message)
                message = input(">")
                if message == QUIT_MSG:
                    connected = False
                connection.sendall(message.encode())
