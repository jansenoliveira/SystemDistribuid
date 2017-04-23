import socket

HOST = '127.0.0.1'
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST,PORT)
print("Para sair, aperte CTRL+X\n")
msg = raw_input()
while msg != '\x18':
	udp.sendto(msg,dest)
	msg = raw_input()
upd.close()