import socket

TCP_IP = '192.168.0.10'
TCP_PORT = 5005
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((TCP_IP, TCP_PORT))


# l="hello"
# print(l)

l="Connection is Up and Running"
l = l.replace(" ","_")
client.send(l.encode())
data = client.accept(BUFFER_SIZE).decode()

client.send(l.encode())
# print(client.send(l.encode()))
data = client.accept(BUFFER_SIZE).decode()
# print("received data:", data)
client.send(l.encode())
# print(client.send(l.encode()))
data = client.accept(BUFFER_SIZE).decode()
client.close()