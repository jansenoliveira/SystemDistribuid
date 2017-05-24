# MOM (Message-Oriented Middleware)

- [https://www.rabbitmq.com/tutorials/tutorial-one-python.html](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)

## Pré-requisitos

Este tutorial pressupõe que o RabbitMQ está instalado e em execução em localhost na porta padrão (5672). No caso de você usar um host diferente, porta ou credenciais, configurações de conexões exigiria ajuste.

### RabbitMQ Pika

RabbitMQ fala AMQP 0.9.1, que é um protocolo aberto, de propósito geral para mensagens. Há uma série de clientes para RabbitMQ em muitos idiomas diferentes. Nesta série tutorial vamos usar Pika, que é o cliente Python recomendado pela equipe RabbitMQ. Para instalá-lo você pode usar a ferramenta de gerenciamento de pacotes pip.

## Tutorial

RabbitMQ é um mediador de mensagens: aceita e encaminha mensagens. Você pode pensar sobre isso como uma agência postal: quando você coloca o e-mail que você deseja postar em uma caixa de correio, você pode ter certeza de que o Sr. Carteiro acabará por entregar o e-mail para o seu destinatário. Nesta analogia, RabbitMQ é uma caixa postal, um posto de correios e um carteiro.

A principal diferença entre RabbitMQ e os correios é que ele não lida com papel, em vez disso ele aceita, armazena e envia blobs binários de dados - mensagens.

RabbitMQ, e mensagens em geral, usa algum jargão.

Produzir nada mais significa que enviar. Um programa que envia mensagens é um produtor

- `P`

Uma fila é o nome para uma caixa de correio que vive dentro de RabbitMQ. Embora o fluxo de mensagens através de RabbitMQ e seus aplicativos, eles só podem ser armazenados dentro de uma fila. Uma fila é limitada apenas pela memória do host e limites de disco, é essencialmente um buffer de mensagens grandes. Muitos produtores podem enviar mensagens para uma fila e muitos consumidores podem tentar receber dados de uma fila. É assim que representamos uma fila:

- `queue_name`

Consumir tem um significado semelhante ao de receber. Um consumidor é um programa que espera principalmente para receber mensagens:

- `C`

Observe que o produtor, consumidor e corretor não precisam residir no mesmo host; Na maioria das aplicações eles não residem.

## Hello World!

(Usando o cliente pika Python 0.10.0)

Nesta parte do tutorial vamos escrever dois pequenos programas em Python; Um produtor (remetente) que envia uma única mensagem e um consumidor (receptor) que recebe mensagens e as imprime. É um "Hello World" de mensagens.

No diagrama abaixo, "P" é nosso produtor e "C" é nosso consumidor. A caixa no meio é uma fila - um buffer de mensagem que RabbitMQ mantém em nome do consumidor.

Nosso projeto geral será parecido com:

- `P -> HELLO -> C`

O produtor envia mensagens para a fila "HELLO". O consumidor recebe mensagens dessa fila.

## Sending

- `P -> HELLO`

Nosso primeiro programa send.py enviará uma única mensagem para a fila. A primeira coisa que precisamos fazer é estabelecer uma conexão com o servidor RabbitMQ.

```python
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
```

Estamos conectados agora, a um **BROKER** na máquina local - daí o localhost. Se quisesse conectar-se a um **BROKER** em uma máquina diferente, simplesmente especificaríamos seu nome ou endereço IP aqui.

Em seguida, antes de enviar, precisamos certificar-nos de que a fila de destinatários existe. Se enviarmos uma mensagem para um local não existente, o RabbitMQ irá simplesmente soltar a mensagem. Vamos criar uma fila hello para a qual a mensagem será entregue:

```python
channel.queue_declare(queue='hello')
```

Neste ponto, estamos prontos para enviar uma mensagem. Nossa primeira mensagem apenas conterá uma string Hello World! E queremos enviá-lo para nossa fila HELLO.

Em RabbitMQ uma mensagem nunca pode ser enviada diretamente para a fila, ele sempre precisa passar por uma troca. Mas não vamos ser arrastados pelos detalhes - você pode ler mais sobre trocas na terceira parte deste tutorial. Tudo o que precisamos saber agora é como usar uma troca padrão identificada por uma seqüência vazia. Esta troca é especial - nos permite especificar exatamente a que fila a mensagem deve ir. O nome da fila precisa ser especificado no parâmetro routing_key:

```python
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
```

Antes de sair do programa, precisamos nos certificar de que os buffers de rede foram limpos e nossa mensagem foi entregue a RabbitMQ. Podemos fazê-lo fechando suavemente a conexão.

```python
connection.close()
```

## Receiving

- `HELLO -> C`

Nosso segundo programa receive.py receberá mensagens de fila e como imprimir na tela

Novamente, primeiro precisamos nos conectar ao servidor RabbitMQ. O código responsável pela conexão com o Rabbit é o mesmo que anteriormente.

A próxima etapa, assim como antes, é certificar-se de que a fila existe. Criar uma fila usando queue_declare é idempotent - podemos executar o comando quantas vezes quisermos, e apenas um será criado.

```python
channel.queue_declare(queue='hello')
```

**Você pode perguntar por que declaramos a fila novamente - já a declaramos em nosso código anterior. Poderíamos evitar que se tivéssemos a certeza de que a fila já existe. Por exemplo, se o programa send.py foi executado antes. Mas ainda não sabemos com certeza qual programa será executado primeiro. Em tais casos, é uma boa prática para repetir declarando a fila em ambos os programas.**

Receber mensagens da fila é mais complexo. Funciona assinando uma função 'callback' para uma fila. Sempre que recebemos uma mensagem, esta função de retorno de chamada é chamada pela biblioteca Pika. No nosso caso esta função imprimirá na tela o conteúdo da mensagem.

```python
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
```

Em seguida, precisamos informar a RabbitMQ que esta função de retorno de chamada específica deve receber mensagens de nossa fila HELLO:

```python
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
```

Para que o comando seja bem sucedido, temos de ter a certeza de que existe uma fila à qual pretendemos subscrever. Felizmente, estamos confiantes sobre isso - criamos uma fila acima - usando queue_declare.

E, finalmente, entramos em um loop interminável que aguarda dados e executa callbacks sempre que necessário.

```python
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
```

