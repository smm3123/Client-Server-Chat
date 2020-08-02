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

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(ADDRESS)
    print("Connected to: " + HOST + " on port " + str(PORT))
    print("Type /q to quit\nEnter a message to send...")

    connected = True
    while connected:
        message = input(">")

        if message == QUIT_MSG:
            connected = False

        client.sendall(message.encode())
        data = client.recv(1024)
        received_message = data.decode()
        if received_message == QUIT_MSG:
            connected = False
        print(received_message)
