import socket
import sys
from _thread import *

host = ''
port = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for a connection.')

def threaded_client(conn):
    reply = ''
    while True:
        data = conn.recv(2048)
        reply = reply + data.decode('utf-8')
        print(reply)
        if not data:
            print('someone left')
            break
        
        if data.decode('utf-8') == '\r\n':
            conn.sendall(str.encode('Server output: '+reply))
            print(reply)
            reply = ''
    conn.close()

while True:

    conn, addr = s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))

    start_new_thread(threaded_client,(conn,))
