from socket import *
from config import hostname, port

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
host = gethostbyname(hostname)
s.connect((host,port))

s.send(bytes("Hello, world!",encoding="ascii"))
s.send(bytes(10))
s.send(bytes(33))
s.send(bytes([11,12,13,14,1,0]))
s.close()