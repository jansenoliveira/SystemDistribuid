import java.rmi.Remote;
import java.rmi.RemoteException;


//A interface Remote serve para identificar interfaces cujos
//métodos podem ser chamados de uma máquina virtual não-local.
//Qualquer objeto que seja um objeto remoto deve implementar
//direta ou indiretamente essa interface. Somente os métodos
//especificados em uma "interface remota", uma interface que
//extends da java.rmi.Remote estão disponíveis remotamente.
public interface Hello extends Remote {
    String sayHello() throws RemoteException;
}

//https://docs.oracle.com/javase/7/docs/api/java/rmi/registry/Registry.html
//https://docs.oracle.com/javase/7/docs/api/java/rmi/registry/LocateRegistry.html
