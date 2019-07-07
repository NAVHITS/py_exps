import socket
U_PORT = 5555
UDP_IP = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
while True:
    data, addr = sock.recvfrom(1024)
    print "Message: ", data
