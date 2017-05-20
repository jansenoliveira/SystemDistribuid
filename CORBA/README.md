# CORBA

## Implementação:

⋅⋅* O IDL para um simples programa "Hello World"
⋅⋅* Um servidor que cria um objeto e o publica com o serviço de nome usando a server-side implementation padrão (POA)
⋅⋅* Um aplicativo cliente que conhece o nome do objeto, recupera uma referência para ele a partir do serviço de nome e invoca o objeto

A seguir, as instruções para compilar e executar o exemplo:

### Definindo a interface (Hello.idl)

O primeiro passo para criar um aplicativo CORBA é especificar todos os seus objetos e suas interfaces usando a Interface Definition Language (IDL) do OMG. IDL tem uma sintaxe semelhante ao C ++ e pode ser usado para definir módulos, interfaces, estruturas de dados e muito mais. O IDL pode ser mapeado para uma variedade de linguagens de programação. O mapeamento IDL para Java é resumido em IDL para Java Language Mapping Summary.

O Hello.idl é escrito no OMG IDL e descreve um objeto CORBA cuja operação `sayHello()` retorna uma seqüência de caracteres e cujo método `shutdown()` desliga o ORB.

### Implementando o Servidor (HelloServer.java)

O servidor de exemplo consiste em duas classes, o **Servant** e o **Server**. O **Servant**, *HelloImpl*, é a implementação da interface Hello IDL; Cada instância Hello é implementada por uma instância *HelloImpl*. O **Server** é uma subclasse de *HelloPOA*, que é gerada pelo compilador `idlj` a partir do exemplo IDL. O **Servant** contém um método para cada operação IDL, neste exemplo, os métodos `sayHello()` e `shutdown ()`. Os métodos **Servant** são exatamente como métodos Java comuns; O código extra para lidar com o ORB, com empacotamento (marshaling) de argumentos e resultados, e assim por diante, é fornecido pelo skeleton.




- Link para a Documentação:
[http://docs.oracle.com/javase/7/docs/technotes/guides/idl/jidlExample.html](http://docs.oracle.com/javase/7/docs/technotes/guides/idl/jidlExample.html)