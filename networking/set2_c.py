#UDP client
import socket

u_PORT = 5556
udp_IP = '127.0.0.1'
BUF_SIZE = 1024
MSG = "Helo"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
