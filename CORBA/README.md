# CORBA

Para essa implementação, usamos o exemplo criado pela Oracle que pode ser encontrado aqui: 

- [http://docs.oracle.com/javase/7/docs/technotes/guides/idl/jidlExample.html](http://docs.oracle.com/javase/7/docs/technotes/guides/idl/jidlExample.html)

## Implementação:

- O IDL para um simples programa "Hello World"

- Um servidor que cria um objeto e o publica com o serviço de nome usando a server-side implementation padrão (POA)

- Um aplicativo cliente que conhece o nome do objeto, recupera uma referência para ele a partir do serviço de nome e invoca o objeto

A seguir, as instruções para compilar e executar o exemplo:


### Definindo a interface (Hello.idl)

O primeiro passo para criar um aplicativo CORBA é especificar todos os seus objetos e suas interfaces usando a Interface Definition Language (IDL) do OMG. IDL tem uma sintaxe semelhante ao C ++ e pode ser usado para definir módulos, interfaces, estruturas de dados e muito mais. O IDL pode ser mapeado para uma variedade de linguagens de programação. O mapeamento IDL para Java é resumido em IDL para Java Language Mapping Summary.

O Hello.idl é escrito no OMG IDL e descreve um objeto CORBA cuja operação `sayHello()` retorna uma seqüência de caracteres e cujo método `shutdown()` desliga o ORB.

### Implementando o Servidor (HelloServer.java)

O servidor de exemplo consiste em duas classes, o **Servant** e o **Server**. O **Servant**, *HelloImpl*, é a implementação da interface Hello IDL; Cada instância Hello é implementada por uma instância *HelloImpl*. O **Server** é uma subclasse de *HelloPOA*, que é gerada pelo compilador `idlj` a partir do exemplo IDL. O **Servant** contém um método para cada operação IDL, neste exemplo, os métodos `sayHello()` e `shutdown ()`. Os métodos **Servant** são exatamente como métodos Java comuns; O código extra para lidar com o ORB, com empacotamento (marshaling) de argumentos e resultados, e assim por diante, é fornecido pelo skeleton.

A classe HelloServer tem o método main () do servidor, que:

- Cria e inicializa uma instância ORB
- Obtém uma referência ao POA 'root' e ativa o POAManager
- Cria uma instância do Servant (a implementação de um objeto CORBA Hello) e informa o ORB sobre ele
- Obtém uma referência de objeto CORBA para um naming context no qual registrar o novo objeto CORBA
- Obtém o naming context 'root'
- Registra o novo objeto no naming context sob o nome de "Hello"
- Espera para invocações do novo objeto do cliente


### Implementando o aplicativo cliente (HelloClient.java)

O cliente exemplo possui:

- Cria e inicializa um ORB
- Obtém uma referência ao naming context da 'root'
- Faz um lookup "Hello" no naming context e recebe uma referência a esse objeto CORBA
- Invoca as operações `sayHello()` e `shutdown()` do objeto e imprime o resultado

Apesar do seu design simples, o programa Hello World permite que você aprenda e experimente todas as tarefas necessárias para desenvolver quase qualquer programa CORBA que use a *invocação estática*. A invocação estática, que usa um *stub* de cliente para a invocação e um *skeleton* de servidor para o serviço sendo invocado, é usada quando a interface do objeto é conhecida em tempo de compilação. Se a interface não for conhecida em tempo de compilação, a *invocação dinâmica* deve ser usada.

Este exemplo requer um *naming service*, que é um serviço CORBA que permite que objetos CORBA sejam nomeados por meio de vinculação (*binding*) de um nome a uma referência de objeto. O *name binding* pode ser armazenada no *naming service* e um cliente pode fornecer o nome para obter a referência de objeto desejada. As duas opções de *naming services* fornecidas com esta versão do Java SE incluem o `orbd`, um processo do daemon que contém um *Serviço de Bootstrap*, um *transient naming service*, um *persistent naming service* um *Server Manager* e *tnameserv*, um *transient naming service* que é fornecido para compatibilidade com versões anteriores. Este exemplo usa `orbd`.

To run this client-server application on your development machine:

1. Altere para o diretório que contém o arquivo Hello.idl.
2. Execute o compilador IDL-to-Java, `idlj`, no arquivo IDL para criar *stubs* e *skeletons*. Esta etapa pressupõe que você tenha incluído o caminho para o diretório java / bin em seu caminho.

```
idlj -fall  Hello.idl
```

Você deve usar a opção `-fall` com o compilador `idlj` para gerar o *client* e *server-side binding*. Essa linha de comando irá gerar as default server-side binding, o que pressupõe o modelo do server-side da herança POA. Para obter mais informações sobre as opções idlj, consulte Opções do compilador IDL-to-Java.

O compilador idlj gera um número de arquivos. O número real de arquivos gerados depende das opções selecionadas quando o arquivo IDL é compilado. Os arquivos gerados fornecem funcionalidade padrão, portanto, você pode ignorá-los até que seja hora de implantar e executar seu programa. Os arquivos gerados pelo compilador idlj para Hello.idl, com a opção de linha de comando -fall, são:

- HelloPOA.java
Esta classe abstrata é o skeleton do servidor baseado em fluxo, fornecendo funcionalidade CORBA básica para o servidor. Ele herda org.omg.PortableServer.Serva nt, e implementa a interface InvokeHandler e a interface HelloOperations. A classe de servidor HelloImpl herda HelloPOA.

- _HelloStub.java
Esta classe é o stub do cliente, fornecendo funcionalidade CORBA para o cliente. Ele herda o `org.omg.CORBA.portable.ObjectImpl` e implementa a interface `Hello.java`.

- Hello.java
Esta interface contém a versão Java da nossa interface IDL. A interface Hello.java extends o org.omg.CORBA.Object, fornecendo a funcionalidade padrão do objeto CORBA. Também extends a interface `HelloOperations` e `org.omg.CORBA.portable.IDLEntity`.

- HelloHelper.java
Esta classe fornece funcionalidade auxiliar, notavelmente o método `narrow()` requerido para converter referências de objeto CORBA para seus tipos apropriados. A classe Helper é responsável por ler e gravar o tipo de dados em fluxos CORBA e inserir e extrair o tipo de dados de Anys. A classe Holder delega os métodos na classe Helper para leitura e escrita.

- HelloHolder.java
Esta classe final contém um membro de instância pública do tipo Hello. Sempre que o tipo IDL é um parâmetro out ou inout, a classe Holder é usada. Ele fornece operações para os argumentos `org.omg.CORBA.portable.OutputStream` e `org.omg.CORBA.portable.InputStream`, que o CORBA permite, mas que não mapeiam facilmente a semântica do Java. A classe Holder delega os métodos na classe Helper para leitura e escrita. Ele implementa `org.omg.CORBA.portable.Streamable`.

- HelloOperations.java
Esta interface contém os métodos `sayHello()` e `shutdown()`. O mapeamento IDL para Java coloca todas as operações definidas na interface IDL nesse arquivo, que é compartilhado pelos stubs e skeletons.


3. Compile os arquivos .java, incluindo os stubs e esqueletos (que estão no diretório HelloApp). Esta etapa assume que o diretório java / bin está incluído no seu path.

```
javac *.java HelloApp/*.java
```

4. Start orbd.

```
orbd -ORBInitialPort 1050&
```

Observe que 1050 é a porta na qual você deseja que o servidor de nomes seja executado. O argumento -ORBInitialPort é um argumento de linha de comando necessário. 

5. Start the Hello server.

```
java HelloServer -ORBInitialPort 1050 -ORBInitialHost localhost&
```

Você verá "HelloServer ready and waiting..." quando o servidor for iniciado.

Para este exemplo, você pode omitir -ORBInitialHost localhost desde que o servidor de nomes está sendo executado no mesmo host que o servidor Hello. Se o servidor de nomes estiver em execução em um host diferente, use-ORBInitialHost nameserverhost para especificar o host no qual o servidor de nome IDL está sendo executado.

Especifique a porta do servidor de nomes (orbd) como feito na etapa anterior, por exemplo, -ORBInitialPort 1050.

6. Run the client application.

```
 java HelloClient -ORBInitialPort 1050 -ORBInitialHost localhost
```

Quando o cliente estiver em execução, você verá uma resposta como a seguinte em seu terminal: "Obtained a handle on server object: IOR: (binary code) Hello World! HelloServer exiting..."

Para este exemplo, você pode omitir -ORBInitialHost localhost desde que o servidor de nomes está sendo executado no mesmo host que o cliente Hello. Se o servidor de nomes estiver em execução em um host diferente, use-ORBInitialHost nameserverhost para especificar o host no qual o servidor de nome IDL está sendo executado.

Especifique a porta do servidor de nomes (orbd) como feito na etapa anterior, por exemplo, -ORBInitialPort 1050.

7. Encerrando o servidor.

Quando tiver terminado este tutorial, certifique-se de desligar ou matar o servidor de nomes (orbd). Para fazer isso a partir de um prompt do DOS, selecione a janela que está executando o servidor e digite Ctrl + C para desligá-lo. Para fazer isso a partir de um shell Unix, localize o processo e mate-o. O servidor continuará a esperar por invocações até que seja explicitamente interrompido.



Copyright © 1993, 2014, Oracle and/or its affiliates. All rights reserved.