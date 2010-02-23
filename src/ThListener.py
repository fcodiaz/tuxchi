import cPickle
import socket
from threading import Thread

import comun
#from Contactos import Contactos
from Mensaje import Mensaje

class ListenerError(Exception):
    def __init__(self,m):
        self.__mensaje = m
    
    def mensaje(self):
        return self.__mensaje
    
class A(Thread):
    def __init__(self, c):
        Thread.__init__(self)
        self._cliente = c
        self.setDaemon(True)
    
    def run(self):
        while 1:
            m = self._cliente.recv(1024)
            if not m: break
            print cPickle.loads(m)  # FIXME: el id que identifica a cada mensaje esta erroneo,
        self._cliente.close()       # creo que deberia venir del numero secuencial de una base de datos
                                    # de preferencia, para evitar duplicacion de id de mensajes.

class Listener:
    BUFF = 1024
    def __init__(self, port, limit):
        self.procesos = []
        self.banderas = []
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
            self.procesos.append(A(cliente).start())
            print self.procesos #FIXME: los procesos se agregan como None a la lista.
            


            #mensaje = cPickle.loads(datos)
            
if __name__ == '__main__':
    
    l = Listener(65432,5)
    l.run()
