# MOM (Message-Oriented Middleware)


## Pré-requisitos

Este tutorial pressupõe que o RabbitMQ está instalado e em execução em localhost na porta padrão (5672). No caso de você usar um host diferente, porta ou credenciais, configurações de conexões exigiria ajuste.


## Tutorial

RabbitMQ é um mediador de mensagens: aceita e encaminha mensagens. Você pode pensar sobre isso como uma agência postal: quando você coloca o e-mail que você deseja postar em uma caixa de correio, você pode ter certeza de que o Sr. Carteiro acabará por entregar o e-mail para o seu destinatário. Nesta analogia, RabbitMQ é uma caixa postal, um posto de correios e um carteiro.

A principal diferença entre RabbitMQ e os correios é que ele não lida com papel, em vez disso ele aceita, armazena e envia blobs binários de dados - mensagens.

RabbitMQ, e mensagens em geral, usa algum jargão.

Produzir nada mais significa que enviar. Um programa que envia mensagens é um produtor

Uma fila é o nome para uma caixa de correio que vive dentro de RabbitMQ. Embora o fluxo de mensagens através de RabbitMQ e seus aplicativos, eles só podem ser armazenados dentro de uma fila. Uma fila é limitada apenas pela memória do host e limites de disco, é essencialmente um buffer de mensagens grandes. Muitos produtores podem enviar mensagens para uma fila e muitos consumidores podem tentar receber dados de uma fila. É assim que representamos uma fila: