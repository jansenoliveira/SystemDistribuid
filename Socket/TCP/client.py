import socket

HOST = '127.0.0.1' 	# Endereco IP do Servidor.
PORT = 5000			# Porta que o Endereco IP esta localizada.

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
#O segundo indica que ele vai se comunicar usando o protocolo TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST,PORT)
tcp.connect(dest)

print("Para sair, use CTRL+X\n")

msg=raw_input()
while msg != '\x18':
	tcp.send(msg)
	msg = raw_input()
	
tcp.close()