#UDP server
import socket

U_PORT = 5555
UDP_IP = "127.0.0.1"
BUF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
while True:
    data, addr = sock.recvfrom(BUF_SIZE)
    print "Message: ", data
