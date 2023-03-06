import socket

UDP_IP = "192.1.1.30"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

print(sock.sendto(MESSAGE, (UDP_IP, UDP_PORT)))