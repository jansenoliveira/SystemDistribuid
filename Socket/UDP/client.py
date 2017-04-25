# -*- coding: utf-8 -*-
import socket

HOST = '127.0.0.1'
PORT = 5000

#https://docs.python.org/2/library/socket.html#module-socket

"""
- Se foi fornecido um nome de hospedeiro converter em endereço IP;
- Se foi fornecido um nome de protocolo de transporte converter em número;
- Criar o socket (função socket);
- Conecta com o servidor (função connect);
- Enviar/Receber dados (permanecer nesse passo enquanto tiver dados para enviar/receber);
- Fechar o socket.
"""

# A função socket() Retorna um objeto de socket cujos 
# métodos implementam as várias chamadas de sistema de socket

#O primeiro parametro AF_INET É usado, se você quiser se comunicar usando protocolos Internet: TCP ou UDP.
#O segundo indica que ele vai se comunicar usando o protocolo UDP.
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST,PORT)

print("Para sair, aperte CTRL+X\n")
msg = raw_input()
while msg != '\x18':
	udp.sendto(msg,dest)
	msg = raw_input()
udp.close()