#TCP client
import socket
T_PORT = 5006
TCP_IP = '127.0.0.1'
BUF_SIZE = 1024
MSG = "Helo"
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, T_PORT))
sock.send(MSG)
data = sock.recv(BUF_SIZE)
sock.close()