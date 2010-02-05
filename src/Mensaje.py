
import comun
import hashlib
from Contactos import Contactos
from Usuario import Usuario

class MensajeError(Exception):
    def __init__(self,m):
        self.__mensaje = m
    
    def mensaje(self):
        return self.__mensaje

class Mensaje:
    def __init__(self, mens, remite, destino,):