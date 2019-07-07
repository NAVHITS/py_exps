#TCP server
import socket
T_PORT = 60
TCP_IP = '127.0.0.1'
BUF_SIZE = 30
sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, T_PORT))
sock.listen(1)
con, addr = sock.accept()
print ('Connection Address is: ' , addr)
while True :
    data = con.recv(BUF_SIZE)
if not data:
    break
print ("Received data", data)
con.send(data)
con.close()