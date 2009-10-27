#!/usr/bin/env python

import comun

class Contactos:
    def __init__(self, prop):
        self.propietario = prop # ID del usuario dueno de la lista de contactos
        self.lista = {}
        
        
    def agregaContacto(self,id,nombre,estado):
        # Lo primero que tenemos que hacer es verificar que este ID de usuario
        # existe en la base de datos de usuarios, de lo contrario, no se puede
        # agregar, pero se sugiere se mande un correo al usuario.
        # Para hacer eso es necesario hacer una consulta al servidor, enviandole 
        # el username del contacto
        print "Dentro de agrega contacto"
        return False
        
        
        # Antes de agregar el contacto es necesario verificar que no esta en la
        # lista de contactos, de lo contrario no se agrega.
        
        # Luego es importante ver que no nos estamos agregando a nosotros mismos
        # como contacto de nosotros mismos, eso no es posible.
    
    def eliminaContacto(self, id):
        print "Dentro de elimina contacto"
        
    def consultaContacto(self,id):
        return False
    
    def modificaContacto(self, id):
        print "Dentro de modifica contacto"
        
    def enviaMensaje(self, id, mens):
        print "Dentro de envia mensaje"
        
    def solicitaAutorizacion(self, id):
        print "Dentro de envia mensaje"
        
    def aceptaAutorizacion(self, id):
        print "Dentro de acepta autorizacion"
    
    def __existe(self, id):
        '''
        Solo es necesario ver si el ID de este usuario se encuentra entre las 
        llaves del diccionario de contactos.
        '''
        return True

    def __mismo(self):
        '''
        El proposito de este metodo privado es que la lista de contactos no puede 
        tener como contacto al duenio de la misma.
        '''
        return True
        
    def devuelveContactos(self):
        return self.lista
        
    def duenoContactos(self):
        '''
        El proposito de este metodo es devolver el ID del usuario propietario de 
        esta lista de contactos. 
        '''
        return self.propietario
    
if __name__ == '__main__':
    print "Nothing"