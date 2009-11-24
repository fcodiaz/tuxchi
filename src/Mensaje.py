
import comun
import hashlib
from Contactos import Contactos
from Usuario import Usuario

class ServidorError(Exception):
    def __init__(self,m):
        self.__mensaje = m
    
    def mensaje(self):
        return self.__mensaje

class Servidor: