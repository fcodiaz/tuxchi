import hashlib
import socket
import cPickle


import comun
#from Contactos import Contactos
from Mensaje import Mensaje

class ListenerError(Exception):
    def __init__(self,m):
        self.__mensaje = m
    
    def mensaje(self):
        return self.__mensaje
    
class Listener:
    BUFF = 1024
    def __init__(self, port, limit):
        self._port = port
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        self._server.bind(('127.0.0.1',self._port))
        self._server.listen(limit)
        
    def run(self):
        "Ciclo principal que se encargara de recibir los mensajes indefinidamente"
        print "Esperando mensajes en el puerto: ", self._port,'\n'
        while True:
            cliente, direccion = self._server.accept()
            print 'Conectado desde ', direccion
            while 1:
                m = cliente.recv(1024)
                if not m: break
                print cPickle.loads(m)
            cliente.close()

            #mensaje = cPickle.loads(datos)
            
if __name__ == '__main__':
    
    l = Listener(65432,5)
    l.run()
