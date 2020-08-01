"""
Name: Syed Mahdi
Date: 8/1/2020
Course: CS 372

Sources:
1) https://realpython.com/python-sockets/
2) https://docs.python.org/3.4/howto/sockets.html
"""

import socket

HOST = "127.0.0.1"
PORT = 65432
ADDRESS = (HOST, PORT)
QUIT_MSG = "/q"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(ADDRESS)
    s.sendall(b"Test message")
    data = s.recv(1024)

print('Received', repr(data))