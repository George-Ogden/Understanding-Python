from socket import *
from config import hostname, port

with socket(AF_INET, SOCK_STREAM) as s:
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((hostname,port))
    s.listen()
    conn, addr = s.accept()
    while True:
        data = conn.recv(32)
        if not data:
            break
        print(data)