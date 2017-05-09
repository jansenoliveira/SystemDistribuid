from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

#https://docs.python.org/2/library/simplexmlrpcserver.html

# Restringir a um caminho especifico
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Criar o servidor
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)

#Registrar as funcoes de introspeccao XML-RPC system.listMethods, system.methodHelp e system.methodSignature
server.register_introspection_functions()


# Registro de pow() funcao; Isso usara o valor de
# pow .__ name__ como o nome, que e apenas 'pow'.
server.register_function(pow)


# Registrar uma funcao com um nome diferente
def adder_function(x,y):
    return x + y
server.register_function(adder_function, 'add')


# Registrar uma instancia; Todos os metodos da instancia sao
# publicado como XML-RPC metodos (neste caso, apenas 'div').
class MyFuncs:
    def div(self, x, y):
        return x // y

server.register_instance(MyFuncs())

# Executar o loop principal do servidor para para sempre e mais 5 dias :D
server.serve_forever()