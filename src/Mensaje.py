#######################################################################
# Esta clase Mensaje funcionada como la clase base para los diferentes tipos
# de mensajes, como seran mensajes de control, estadus, mensajes, autenticacion.
# 
#
#
#
#
import comun
import hashlib
import cPickle

#from Contactos import Contactos
#from Usuario import Usuario

class MensajeError(Exception):
    def __init__(self,m):
        self.__mensaje = m
    
    def mensaje(self):
        return self.__mensaje

class Mensaje:
    _seqID = 0
    def __init__(self,tipo, orig, dest,mens=''):
        self._mid = Mensaje._seqID
        self.increaseID()
        self._tipo = tipo #Control, Mensaje, Estatus, Autenticacion.
        self._origen = orig  # Quien envia el mesaje
        self._destino = dest # A quien se dirige el mensaje
        self._mensaje = mens # Texto del mensaje a transmitir
        
    def increaseID(self):
        Mensaje._seqID = Mensaje._seqID + 1
        
    def __str__(self):
        return "id: %d \nDest: %d \nMensaje: %s" % (self._mid, self._destino, self._mensaje)
        

if __name__ == '__main__':
    m1 = Mensaje(0,2,5,"Este es un mensaje de prueba")
    bytes = cPickle.dumps(m1)
    print cPickle.loads(bytes)
    m2 = Mensaje(0,2,3,"Este es otro mensaje de prueba")
    m3 = Mensaje(0,2,5,"Tercer mensaje de prueba")
    m4 = Mensaje(0,2,10,"Cuarto mensaje de prueba")
    print m4
