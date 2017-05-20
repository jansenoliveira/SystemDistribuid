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

A classe HelloServer tem o método main () do servidor, que:

⋅⋅* Cria e inicializa uma instância ORB
⋅⋅* Obtém uma referência ao POA 'root' e ativa o POAManager
⋅⋅* Cria uma instância do Servant (a implementação de um objeto CORBA Hello) e informa o ORB sobre ele
⋅⋅* Obtém uma referência de objeto CORBA para um naming context no qual registrar o novo objeto CORBA
⋅⋅* Obtém o naming context 'root'
⋅⋅* Registra o novo objeto no naming context sob o nome de "Hello"
⋅⋅* Espera para invocações do novo objeto do cliente


### Implementando o aplicativo cliente (HelloClient.java)

O cliente exemplo possui:

⋅⋅* Cria e inicializa um ORB
⋅⋅* Obtém uma referência ao naming context da 'root'
⋅⋅* Faz um lookup "Hello" no naming context e recebe uma referência a esse objeto CORBA
⋅⋅* Invoca as operações `sayHello()` e `shutdown()` do objeto e imprime o resultado

Apesar do seu design simples, o programa Hello World permite que você aprenda e experimente todas as tarefas necessárias para desenvolver quase qualquer programa CORBA que use a *invocação estática*. A invocação estática, que usa um *stub* de cliente para a invocação e um *skeleton* de servidor para o serviço sendo invocado, é usada quando a interface do objeto é conhecida em tempo de compilação. Se a interface não for conhecida em tempo de compilação, a *invocação dinâmica* deve ser usada.

Este exemplo requer um *naming service*, que é um serviço CORBA que permite que objetos CORBA sejam nomeados por meio de vinculação (*binding*) de um nome a uma referência de objeto. O *name binding* pode ser armazenada no *naming service* e um cliente pode fornecer o nome para obter a referência de objeto desejada. As duas opções de *naming services* fornecidas com esta versão do Java SE incluem o `orbd`, um processo do daemon que contém um *Serviço de Bootstrap*, um *transient naming service*, um *persistent naming service* um *Server Manager* e *tnameserv*, um *transient naming service* que é fornecido para compatibilidade com versões anteriores. Este exemplo usa `orbd`.





- Link para a Documentação:
[http://docs.oracle.com/javase/7/docs/technotes/guides/idl/jidlExample.html](http://docs.oracle.com/javase/7/docs/technotes/guides/idl/jidlExample.html)