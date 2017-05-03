import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {

    private Client() {}

    public static void main(String[] args) {

	String host = (args.length < 1) ? null : args[0];
	try {
		//Retorna uma referência para o objeto remoto Registry
		//no host especificado na porta Registro usar como padrão de 1099.
	    Registry registry = LocateRegistry.getRegistry(host);

	    //Retorna a referência remota vinculada ao nome especificado neste Registro.
	    Hello stub = (Hello) registry.lookup("Hello");

	    //Chama o método que retorna o "Olá, amiguinho!" da referencia remota 
	    String response = stub.sayHello();
	    System.out.println("resposta servidor: " + response);
	} catch (Exception e) {
	    System.err.println("Client exception: " + e.toString());
	    e.printStackTrace();
	}
    }
}