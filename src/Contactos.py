#!/usr/bin/env python
# Autor: Fco Diaz
# Fecha: Oct/2009
# Detalles: la clase Contactos esta destinada a brindar toda la funcionalidad
# necesaria a la lista de contactos de cada usuario; esta se encuentra en el 
# cliente.


import comun

class ContactosError(Exception):
    def __init__(self,m):
        self.__mensaje = m
    
    def mensaje(self):
        return self.__mensaje

class Contactos:
    def __init__(self, prop):
        self.__propietario = prop # ID del usuario dueno de la lista de contactos
        self.__lista = {}         # La lista de contactos sera un Diccionario donde el id del usuario
                                  # sera la llave de sus datos.
        
        
    def agregaContacto(self, id, nombre, estado=comun.ESTADOS.DESCONECTADO, mensaje='', imagen=''):
        # Lo primero que tenemos que hacer es verificar que este ID de usuario
        # existe en la base de datos de usuarios, de lo contrario, no se puede
        # agregar, pero se sugiere se mande un correo al usuario.
        # Para hacer eso es necesario hacer una consulta al servidor, enviandole 
        # el username del contacto
        print "Dentro de agrega contacto"
        if self.__mismo(id):      # Verificamos que el contacto no soy yo mismo
            raise ContactosError("No se puede agregar al mismo usuario como contacto de si mismo")
        elif self.__existe(id):   # Verificamos que el contacto no exista previamente en la lista
            raise ContactosError("Este contacto ya forma parte de la lista de contactos")
        else:                     # Aqui es donde agregamos el nuevo contacto a nuestra lista
            self.__lista[id] = {"nombre":nombre,"estado":estado,"mensaje":mensaje,"imagen":imagen}
            return True
        
        
        
        # Antes de agregar el contacto es necesario verificar que no esta en la
        # lista de contactos, de lo contrario no se agrega.
        
        # Luego es importante ver que no nos estamos agregando a nosotros mismos
        # como contacto de nosotros mismos, eso no es posible.
    
    def eliminaContacto(self, id):
        print "Dentro de elimina contacto"
        if self.__existe(id):
            return self.__lista.pop(id)
        else:
            raise ContactosError("Numero de identificacion de contacto invalido")
  
    def destruyeContactos(self):
        print "Dentro de destruye contactos"
        self.__lista.clear()
        
    def cuentaContactos(self):
        print "Dentro de cuenta contactos"
        return len(self.__lista)
        
    
    def consultaContacto(self,id):
        if self.__existe(id):
            return (id, self.__lista[id]["nombre"])
        else:
            raise ContactosError("Numero de identificacion de  invalido")
        
    def consultaEstado(self, id):
        if self.__existe(id):
            return (self.__lista["estado"])
        else:
            raise ContactosError("Contacto no existe en lista de contactos")
    
    def modificaNombre(self, id, nombre):
        print "Dentro de modifica nombre"
        # Seria bueno verificar que se esta dando de nombre nuevo, algunas caracteristicas que debe cumplir
        #  - Que sea minimo 3 letras o numeros
        #  - Otra caracteristica?
        assert (len(name) > 2), "Nombre del contacto no puede ser menor que 3 caracteres"
        
        if self.__existe(id):
            self.__lista[id] ["nombre"] = nombre  
            return (id, self.__lista[id]["nombre"])
        else:
            raise ContactosError("Numero de identificacion de  invalido")
        
    def modificaEstado(self,id,estado):
        print "Dentro de modifica estado"
        if estado in comun.ESTADOS:
            if self.__existe(id):
                self.__lista[id] ["estado"] = estado  
                return (id, self.__lista[id]["mensaje"])
            else:
                raise ContactosError("Numero de identificacion de  invalido")  
        else: raise ContactosError("Este no es un estado valido del sistema")
        
    def modificaMensaje(self,id,mensaje):
        print "Dentro de modifica mensaje"
        # Seria bueno verificar que se esta dando de nombre nuevo, algunas caracteristicas que debe cumplir
        #  - Que sea minimo 3 letras o numeros
        #  - Otra caracteristica?        
        if self.__existe(id):
            self.__lista[id] ["mensaje"] = mensaje  
            return (id, self.__lista[id]["mensaje"])
        else:
            raise ContactosError("Numero de identificacion de  invalido")
        
    def modificaImagen(self,id,imagen):
        print "Dentro de modifica imagen" 
        if self.__existe(id):
            self.__lista[id] ["imagen"] = imagen  
            return (id, self.__lista[id]["imagen"])
        else:
            raise ContactosError("Numero de identificacion de  invalido")
        
    # Creo que envia mensaje es un metodo que no solo necesita saber a que
    # contacto se desea enviar el mensaje, pero tambien la conexion del servidor
    # es importante, dado que es este quien al final se encarga de enviar el
    # mensaje. Asi que creo que uno de los parametros de este metodo debe ser
    # tambien el objeto que se crea e identifica al servidor.
    def enviaMensaje(self, id, mens):
        print "Dentro de envia mensaje"
        # Una de las primeras cosas que se debe hacer es ver el estado del contacto antes de intentar enviar el 
        # mensaje a este usuario. Si el usuario esta Desconectado entonces debe notificarse que no se puede enviar
        # el mensaje. Lo que se puede hacer es guardar el mensaje para mandarlo cuando el usuario este disponible.
        if consultaEstado(id) != comun.ESTADO.DESCONECTAD:
            # Contacta al servidor para enviar el mensaje
            server.enviaMensaje()  #FIXME!!!
        else:
            raise ContactosError("Contacto se encuentra Desconectado, mensaje no fue enviador")
        
                
    def solicitaAutorizacion(self, id):
        print "Dentro de envia mensaje"
    
    def aceptaAutorizacion(self, id):
        print "Dentro de acepta autorizacion"
    
    def __existe(self, id):
        '''
        Solo es necesario ver si el ID de este usuario se encuentra entre las 
        llaves del diccionario de contactos.
        '''
        return self.__lista.has_key(id)   # Devuelve True en caso que este usuario ya forma parte de los contactos.

    def __mismo(self,id):
        '''
        El proposito de este metodo privado es que la lista de contactos no puede 
        tener como contacto al duenio de la misma.
        '''
        if self.__propietario == id:
            return True
        else: return False
        
    def devuelveContactos(self):
        return self.__lista
        
    def duenoContactos(self):
        '''
        El proposito de este metodo es devolver el ID del usuario propietario de 
        esta lista de contactos. 
        '''
        return self.__propietario
    
if __name__ == '__main__':
    print "Nothing"
