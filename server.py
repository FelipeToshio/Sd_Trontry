import Pyro4

@Pyro4.expose
class Hello(object):
    def say_hello(self):
        return 'Teste'
        
daemon = Pyro4.Daemon()             #cria um daemon do Pyro
ns = Pyro4.locateNS()               #procura o servidor DNS
uri = daemon.register(Hello)        #registra Hello no Pyro
ns.register("example.hello", uri)   #registra Hello no servidor DNS

print("Servidor Pronto.")
daemon.requestLoop()                #inicia a espera por chamadas