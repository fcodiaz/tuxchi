from Comunicador import *
from Contactos import  *
from Mensaje import *

    # El siguiente objeto no puede ser creado sino hasta que el usuario se haya autenticado con el servidor
    # por lo tanto no podemos hacer esta llamada en este momento, sino hasta despues.
    #clienteUsuario = Usuario.Usuario("Nombre","USuario","Contrasenia") 

    # La siguiente llamada a crear los contactos del usuario no se puede hacer pues el usuario
    # aun no ha sido autenticado con el servidor, por tanto no se puede hacer esta llamada.
    #clienteContactos = Contactos.Contactos(UsuarioID) 

    # El sistema iniciara mediante el Interprete de Comandos del cliente, el cual se ejecutara constantemente 
    # a lo largo de que el programa funcione, al mismo tiempo el comunicador del cliente se encargara de mantener 
    # una comunicacion constante con el servidor, asi que una alternativa de mantener ambos procesos funcionando 
    # es mediante el uso de Threads. Un thread se encargaria de controlar al interprete de comandos, y el otro al 
    # comunicador del cliente, los resultados de ambos procesos son objetos tipo mensaje.

class Cliente:
    def __init__(self):

    # Inicio del Cliente
    # 1. clienteComunicator thread starts, inicialmente verifica que hay comunicacion con el servidor y continua, de lo contrario
    # termina con un error indicando que no hay comunicacion con el servidor; a este punto el usuario no se ha conectado.
    # 2. Se da inicio al interprete de comandos mediante un segundo thread, el interprete de comandos se encargara de 
    # autenticar al usuario como primera actividad, el cliente no puede realizar ninguna otra actividad a menos que un usuario
    # haya sido autenticado por medio del servidor.
    # 3. una vez el usuario se ha registrado en el sistema, se crea un objeto Contactos para llevar el control de los contactos
    # del usuario, asi como las acciones que vamos a desarrollar sobre ellos.
    def inicio(self):
        self.__clienteComunicador = Comunicador.Comunicador()        

    # Loop principal del sistema
    # En este loop se colocaran los dos thread que fueron creados al inicio del sistema, y los cuales funcionaran hasta que el cliente
    # sea cerrado, aun si el usuario hace logout, el cliente puede seguir funcionando, en cuyo caso espera a que sea cerrado completamente
    # o el usuario se registre nuevamente.
    def ejecutar(self):
        
    def cerrar(self):
        
    def info(self):
        
    
if __name__ == "__main__":
    miCliente = Cliente()
    try:
        miCliente.inicio()
    except:
        miCliente.cerrar()
        sys.exit(1)
    try:
        micliente.ejecutar()
    except:
        miCliente.cerrar()
        sys.exit(2)
        
    miCliente.cerrar()













