
import comun
import hashlib
from Contactos import Contactos

class UsuarioError(Exception):
    def __init__(self,m):
        self.__mensaje = m
    
    def mensaje(self):
        return self.__mensaje

class Usuario:
    def __init__(self, nombre, usuario, contrasena):
        self.nombre = nombre # Nombre completo: Francisco Diaz
        # self.usuario = usuario # fcodiaz
        self.usuario = hashlib.sha224(usuario) # Para verificar: userID.hexdigest() == hashlib.sha224("user").hexdigest()
        self.contrasena = hashlib.sha224(contrasena)
        self.estado = DESCONECTADO
        self.mensaje = ""
        self.imagen = ""
        self.listaContactos = Contactos(self.usuario)
        
    def enviaMensaje(self, id, mensaje):
        '''
        Este metodo se encarga de enviar un mensaje a uno de los contactos de la lista.
        '''
        print "Dentro de envia mensaje"
        self.listaContactos.enviaMensaje(id,mensaje) # id del contacto a quien se desea enviar mensaje
        
    def recibeMensaje(self):
        '''
        Este metodo se encarga de contactar al servidor y verificar si no hay algun mensaje pendiente
        '''
        print "Dentro de recibe mensaje"
        remite, mensaje = self.__leeColaMensajes()
        
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
        
    def __leeComandos(self):
        print "Dentro de lee comandos del servidor"
        
    def __conectaServer(self):
        print "Dentro de conecta Server"
        
    def __leeColaMensajes(self):
        print "Dentro de lee servidor"
        
    def __sincronizaContactos(self):
        '''
        La idea de este metodo es sincronizar la lista de contactos con la lista que el 
        servidor posee con respecto al estado de los usuarios
        '''
    
    
        