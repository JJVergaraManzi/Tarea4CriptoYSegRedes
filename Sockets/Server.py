import socket

MySocket = socket.socket
MySocket.blind( ('localhost', 8000))
MySocket.listen(5)

while True:
    connection, addr = MySocket.accept()
    print("Conection established")
    print(addr)

    petition = connection.recv(1024)
    print(petition)

    connection.send("Hi")
    connection.close()