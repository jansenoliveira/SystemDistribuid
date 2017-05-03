import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;
	
public class Server implements Hello {
    int cont=0;
    public Server() {}
    public String sayHello() {
    	cont++;
	System.out.println ("atendeu cliente" + cont);
	return "Hello, world!";
    }
    public static void main(String args[]) {
	
	try {
	    Server obj = new Server();
	    Hello stub = (Hello) UnicastRemoteObject.exportObject(obj, 0);

	    // registra o objeto remoto
	    Registry registry = LocateRegistry.getRegistry();
	    registry.bind("Hello", stub);
	    System.err.println("Servidor rodando...");
	} catch (Exception e) {
	    System.err.println("erro no servidor: " + e.toString());
	    e.printStackTrace();
	}
    }
}
