import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;
	
public class Server implements Hello {
    int cont=0;
    public Server() {}

    public String sayHello() {
    	cont++;
	System.out.println ("Atendeu cliente de número: " + cont);
	return "Olá, amiguinho!";
    }
    public static void main(String args[]) {
	
	try {
	    Server obj = new Server();

	    //O método estático UnicastRemoteObject.exportObject exporta o objeto remoto
	    //fornecido para receber invocações de método remoto de entrada em uma porta TCP
	    //anônima e retorna o stub para o objeto remoto para passar para os clientes.
	    //Como resultado da chamada exportObject, o tempo de execução pode começar a escutar
	    //em um novo soquete de servidor ou pode usar um soquete de servidor compartilhado
	    //para aceitar chamadas remotas recebidas para o objeto remoto.
	    //O stub retornado implementa o mesmo conjunto de interfaces remotas como
	    //a classe do objeto remoto e contém o nome do host ea porta sobre as
	    //quais o objeto remoto pode ser contatado.
	    Hello stub = (Hello) UnicastRemoteObject.exportObject(obj, 0);

	    
		//LocateRegistry é usado para obter uma referência a um registro de objeto remoto
		//de bootstrap em um host específico (incluindo o host local) ou para criar um registro
		//de objeto remoto que aceite chamadas em uma porta específica.
	    Registry registry = LocateRegistry.getRegistry(); 	//Retorna uma referência para o 
	    													//registro de objeto remoto para o host
	    													//local na porta de registro padrão de 1099.

	    //bind(String name, Remote obj)
	    registry.bind("Hello", stub); //Vincula uma referência remota para o nome especificado neste Registro
	    System.err.println("Servidor rodando...");
	} catch (Exception e) {
	    System.err.println("Erro no servidor: " + e.toString());
	    e.printStackTrace();
	}
    }
}
