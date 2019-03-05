import socket

TCP_IP = '192.168.0.10'
TCP_PORT = 5005
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((TCP_IP, TCP_PORT))


l="Connection is Up and Running \n"

client.send(l.encode())

# client.send(l.encode())

# client.send(l.encode())

client.close  ()