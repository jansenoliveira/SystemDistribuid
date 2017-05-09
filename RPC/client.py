import xmlrpclib

#https://docs.python.org/2/library/xmlrpclib.html

#Uma instancia ServerProxy e um objeto que gerencia a comunicacao com um
#servidor XML-RPC remoto. O primeiro argumento necessario e um URI (Uniform Resource Indicator)
#e normalmente sera o URL do servidor.
s = xmlrpclib.ServerProxy('http://localhost:8000')
print s.pow(2,3)  # Returns 2**3 = 8
print s.add(2,3)  # Returns 5
print s.div(5,2)  # Returns 5//2 = 2

# Printa todos os metodos disponiveis do servidor
print s.system.listMethods()