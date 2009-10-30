
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
        print "Dentro de envia mensaje"
        
    def cambiaMensaje(self,mensaje):
        print "Dentro de cambia mensaje"
        
    def cambiaContrasena(self, contrasena):
        '''
        Creo que es necesario adelantar que para que la contrasena sea cambiada, con 
        anterioridad debera preguntarse por la contrasenia antigua antes de hacer algun 
        cambio.
        '''
        print "Dentro de cambia contrasena"
        
    def cambiaEstado(self, estado):
        self.estado = estado
        
    def cambiaImagen(self,imagen):
        self.imagen = imagen
        
    def agregaContacto(self,id):
        print "Dentro de agrega contacto"
        
    def eliminaContacto(self,id):
        print "Dentro de eliminacion de contacto"
        
    def conectaServer(self):
        print "Dentro de conecta Server"
        
    def sincronizaContactos(self):
        '''
        La idea de este metodo es sincronizar la lista de contactos con la lista que el 
        servidor posee con respecto al estado de los usuarios
        '''
    
    
        