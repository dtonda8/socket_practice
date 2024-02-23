import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

client.send("Hello, from client!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
client.send("Bye, from client!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
client.close()