import socket

mySocket = socket.socket()
mySocket.bind(("localhost", 9999))
mySocket.listen(3)
while True:
    c, address = mySocket.accept()
    c.recv(1024).decode()
    c.send("Hello client, your message was received successfully".encode()) # Added .encode() to send a byte string
    c.close()