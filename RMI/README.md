# RMI

1. Definir a interface
2. Implementar servidor para objetos remotos
3. Implementar cliente
4. Compilar
5. Iniciar o RMI Registry no servidor
6. Iniciar o servidor de objetos
7. Iniciar o cliente

## Compilar os Arquivos

Onde destDir é o diretório de destino para colocar os arquivos de classe.
```shell
	javac -d destDir Hello.java Server.java Client.java
```

## Start the Java RMI registry

Para iniciar o registro, execute o comando rmiregistry no host do servidor. Este comando não produz saída (quando bem sucedida) e normalmente é executado em segundo plano. Para obter mais informações, consulte a documentação de ferramentas para rmiregistry.
```shell
	rmiregistry &
```
## Start the server

Para iniciar o servidor, execute a classe Server usando o comando java da seguinte maneira:
```shell
	java -classpath ./ -Djava.rmi.server.codebase=file:./ Server &
```
## Run the client


Uma vez que o servidor está pronto, o cliente pode ser executado da seguinte forma:
```shell
	java  -classpath ./ Client
```

## Documentação:
[http://docs.oracle.com/javase/7/docs/technotes/guides/rmi/hello/hello-world.html](http://docs.oracle.com/javase/7/docs/technotes/guides/rmi/hello/hello-world.html)
