import socket
c = socket.socket()
c.connect(("localhost", 9999))
c.send(bytes("Khalid", "utf-8") )
print(c.recv(1024).decode())