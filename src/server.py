"""
Name: Syed Mahdi
Date: 8/1/2020
Course: CS 372

Sources:
1) https://realpython.com/python-sockets/
2) https://docs.python.org/3.4/howto/sockets.html
"""

import socket
from src import constants


def start_server():
    """Initializes server and begins listening"""
    server.bind(constants.ADDRESS)
    server.listen()
    print("Server listening on: " + constants.HOST + " on port " + str(constants.PORT) + "...")


def print_connection_messages():
    print("Connected by", address)
    print("Type /q to quit\nWaiting for message...\n")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    start_server()

    connection, address = server.accept()

    with connection:
        print_connection_messages()
        connected = True

        while connected:
            data = connection.recv(1024)
            if not data:
                continue

            received_message = data.decode()
            print(received_message)

            if received_message == constants.QUIT_MSG:
                connected = False
            else:
                message = input(">")
                if message == constants.QUIT_MSG:
                    connected = False
                connection.sendall(message.encode())
