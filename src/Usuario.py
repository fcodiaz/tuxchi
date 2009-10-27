
import comun
import hashlib
from Contactos import Contactos


class Usuario:
    def __init__(self, nombre, usuario, contrasena):
        self.nombre = nombre # Nombre completo: Francisco Diaz
        # self.usuario = usuario # fcodiaz
        self.usuario = hashlib.sha224(usuario) # Para verificar: userID.hexdigest() == hashlib.sha224("user").hexdigest()
        self.contrasena = hashlib.sha224(contrasena)
        self.estado = DESCONECTADO
        self.mensaje = ""
        self.imagen = ""
        self.listaContactos = Contactos()
        
    def enviaMensaje(self, id):
    '''
    Este metodo se encarga de enviar un mensaje a uno de los contactos de la lista.
    '''