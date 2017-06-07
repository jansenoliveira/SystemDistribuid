from zeep import Client

client = Client('http://127.0.0.1:9876/calc?wsdl')
result = client.service.soma(40,40)

print(result)