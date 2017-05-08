import xmlrpclib

#https://docs.python.org/2/library/xmlrpclib.html

#Uma instância ServerProxy é um objeto que gerencia a comunicação com um
#servidor XML-RPC remoto. O primeiro argumento necessário é um URI (Uniform Resource Indicator)
#e normalmente será o URL do servidor.
s = xmlrpclib.ServerProxy('http://localhost:8000')
print s.pow(2,3)  # Returns 2**3 = 8
print s.add(2,3)  # Returns 5
print s.div(5,2)  # Returns 5//2 = 2

# Printa todos os métodos disponiveis do servidor
print s.system.listMethods()