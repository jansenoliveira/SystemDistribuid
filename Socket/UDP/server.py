# -*- coding: utf-8 -*-
import socket
#https://docs.python.org/2/library/socket.html#module-socket

"""
- Se foi fornecido um nome de protocolo de transporte converter em número;
- Criar o socket (função socket);
- Coloca um endereço local, endereço IP e porta, no socket (função bind);
- Instrui o sistema operacional para colocar o socket em modo passivo (função listen);
- Aceita uma nova conexão (função accept);
- Enviar/Receber dados (permanecer nesse passo enquanto tiver dados para enviar/receber);
- Fechar o socket.
- Volta ao passo 5 para aceitar outra conexão.

Enquanto o servidor atende uma conexão ele fica dedicado a ela.
Para evitar isso é possível fazer um passo intermediário entre o 5 e o 6 para criar um novo processo
ou thread para tratar da nova conexão que esta chegando.
Com isso o processo/thread pai fica somente recebendo as conexões e o processo/thread
filho trata das requisições dos clientes.
"""

HOST = ''
PORT = 5000

# A função socket() Retorna um objeto de socket cujos 
# métodos implementam as várias chamadas de sistema de socket

#AF_INET É usado, se você quiser se comunicar usando protocolos Internet: TCP ou UDP.
#Significa que ele é um soquete UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

# Vincula o socket ao endereço. O socket não deve já estar vinculado.
udp.bind(orig)
while True:

	"""	Receber dados do soquete. O valor de retorno é um par (string, address)
		onde string é uma string representando os dados recebidos e address é o
		endereço do soquete enviando os dados. """
	msg, cliente = udp.recvfrom(1024)
	print cliente, msg
udp.close()