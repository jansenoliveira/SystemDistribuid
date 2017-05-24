
# -*- coding: utf-8 -*-

"""RabbitMQ fala AMQP 0.9.1, que é um protocolo aberto, de propósito geral para mensagens.
Há uma série de clientes para RabbitMQ em muitos linguagens diferentes. Nesta série tutorial vamos usar Pika,
que é o cliente Python recomendado pela equipe RabbitMQ. Para instalá-lo você pode usar a ferramenta de
gerenciamento de pacotes pip."""
import pika


"""Nosso primeiro programa send.py enviará uma única mensagem para a fila.
A primeira coisa que precisamos fazer é estabelecer uma conexão com o servidor RabbitMQ."""

"""Estamos conectados agora, a um broker na máquina local - daí o localhost.
Se quisesse conectar-se a um broker em uma máquina diferente, simplesmente
especificaríamos seu nome ou endereço IP aqui."""
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

"""Em seguida, antes de enviar, precisamos certificar-nos de que a fila de destinatários existe.
Se enviarmos uma mensagem para um local não existente, o RabbitMQ irá simplesmente soltar a mensagem.
Vamos criar uma fila hello para a qual a mensagem será entregue:"""
channel.queue_declare(queue='hello')

"""Neste ponto, estamos prontos para enviar uma mensagem.
Nossa primeira mensagem apenas conterá uma string Hello World!
E queremos enviá-lo para nossa fila hello."""

"""Em RabbitMQ uma mensagem nunca pode ser enviada diretamente para a fila,
ele sempre precisa passar por uma troca. Mas não vamos ser arrastados pelos detalhes
Tudo o que precisamos saber agora é como usar uma troca padrão identificada por uma sequência vazia.
Esta troca é especial - nos permite especificar exatamente a que fila a mensagem deve ir.
O nome da fila precisa ser especificado no parâmetro routing_key:"""
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

"""Antes de sair do programa, precisamos nos certificar de que os buffers de rede foram limpos e nossa
mensagem foi entregue a RabbitMQ. Podemos fazê-lo fechando suavemente a conexão."""
connection.close()