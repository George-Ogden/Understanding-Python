from socket import *
port = 1234

with socket(AF_INET,SOCK_DGRAM) as s:
    s.connect(("192.168.1.1",80))
    host, _ = s.getsockname()

hostname = gethostname()

if __name__ == "__main__":
    print(host)