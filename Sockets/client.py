import socket

MySocket = socket.socket
MySocket.blind( ('localhost', 8000))

MySocket.send("Hi from client")
response= MySocket.recv(1024)

print (response)

MySocket