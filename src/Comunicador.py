import hashlib
import socket
import cPickle

import comun
#from Contactos import Contactos
from Mensaje import Mensaje

class ComunicadorError(Exception):
    def __init__(self,m):
        self.__mensaje = m
    
    def mensaje(self):
        return self.__mensaje
    
class Comunicador:
    BUFF=1024
    
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._cliente.connect((self._host,self._port))
        
    def enviaMensaje(self,m):
        
        datos = cPickle.dumps(m)
        while datos:
            enviados = self._cliente.send(datos[:self.BUFF])
            datos = datos[enviados:]
        if datos:
            return False
        return True
    
    def recibeMensaje(self):
        datos = []
        temp = ''
        while not '\n' in temp:
            try:
                temp = self._cliente.recv(self.BUFF)
                buf.append(temp)
            except socket.error:
                break
        return cPickle.loads(''.join(datos)[:-1])
                
if __name__ == '__main__':
    c = Comunicador('127.0.0.1',65432)
    
    mensajes = [Mensaje(0,2,5,"Este es un mensaje de prueba"),\
    Mensaje(0,2,3,"Este es otro mensaje de prueba"),\
    Mensaje(0,2,5,"Tercer mensaje de prueba"),\
    Mensaje(0,2,10,"Cuarto mensaje de prueba")]
    
    for m in mensajes:
        print 'Enviando mensaje ', m
        c.enviaMensaje(m)
    texto='Dummy'
    while texto:
        texto = raw_input("Mensaje a enviar: ")
        m = Mensaje(0,2,5,texto)
        c.enviaMensaje(m)
    
