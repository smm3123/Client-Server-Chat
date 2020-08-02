# Client-Server-Chat

A simple client-server chat application that runs locally on your machine. This is application is an exercise in socket programming with Python.

## Running the Program
If your IDE supports running multiple programs at once, you can run server.py and then client.py to set everything up. If your IDE doesn't support this, you can follow these steps...

In your IDE, run server.py. The following message should appear in the terminal:

```shell
Server listening on: localhost on port 65432...
```

After this message appears, open up the directory that client.py is in within a terminal and run the following command:

```shell
python client.py
```

The following message should appear in the terminal, letting you know the client has connected properly:

```shell
Connected to: localhost on port 65432
Type /q to quit
Enter a message to send...
```

From here, you can send messages to and from the server.
