# -*- coding: utf-8 -*-
import pika


"""A primeira coisa que precisamos fazer é estabelecer uma conexão com o servidor RabbitMQ.
Estamos conectados agora, a um broker na máquina local - daí o localhost.
Se quisesse conectar-se a um broker em uma máquina diferente, simplesmente
especificaríamos seu nome ou endereço IP aqui."""
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

"""A próxima etapa é certificar-se de que a fila existe.
Criar uma fila usando queue_declare é 'idempotent' - podemos executar o comando
quantas vezes quisermos, e apenas um será criado"""
channel.queue_declare(queue='hello')

##### APENAS PARA ESCLARECIMENTO ####
"""Você pode perguntar por que declaramos a fila novamente - já a declaramos em nosso código send.py.
Poderíamos evitar que se tivéssemos a certeza de que a fila já existe.
Por exemplo, se o programa send.py foi executado antes.
Mas ainda não sabemos com certeza qual programa será executado primeiro.
Em tais casos, é uma boa prática para repetir declarando a fila em ambos os programas."""
#####################################

"""Receber mensagens da fila é mais complexo.
Ele funciona assinando (subscribing) uma função de retorno de chamada (callback) em uma fila.
Sempre que recebemos uma mensagem, esta função de callback será chamada pela biblioteca Pika.
No nosso caso esta função imprimirá na tela o conteúdo da mensagem."""
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

"""Em seguida, precisamos informar a RabbitMQ que esta função de callback
específica deve receber mensagens de nossa fila HELLO"""

"""
Para que o comando seja bem sucedido, temos de ter a certeza de que existe
uma fila à qual pretendemos subscrever. Felizmente, estamos confiantes sobre isso
- criamos uma fila acima - usando queue_declare."""
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

"""E, finalmente, entramos em um loop interminável que aguarda dados e executa callbacks sempre que necessário."""
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()