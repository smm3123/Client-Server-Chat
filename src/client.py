"""
Name: Syed Mahdi
Date: 8/1/2020
Course: CS 372
"""

import socket
from src import constants


def connect_client():
    client.connect(constants.ADDRESS)
    print("Connected to: " + constants.HOST + " on port " + str(constants.PORT))
    print("Type /q to quit\nEnter a message to send...\n")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    connect_client()

    connected = True
    while connected:
        message = input(">")

        client.sendall(message.encode())
        received_message = client.recv(1024).decode()
        print(received_message)

        if received_message == constants.QUIT_MSG or message == constants.QUIT_MSG:
            connected = False
