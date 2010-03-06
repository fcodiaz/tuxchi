



import comun
import hashlib
from Contactos import Contactos

COMANDOS_VALIDOS = ['contacto','estado','mensaje','ingreso']

class ComandosError(Exception):
    def __init__(self,m):
        self.__mensaje = m
    
    def mensaje(self):
        return self.__mensaje
    
class Comandos:
    def __init__(self, modo, usuario,simbolo = "> "): # Modo, Usuario, simbolo
        """
        Modo indicara si el interprete de comandos esta en modo interactivo o no
        """
        assert modo == 1 or modo == 0, "Modo de interprete de comandos incorrecto"  # 0: interactivo, 1: no interactivo
        self._modo = modo
        self._simbolo = simbolo # El indicador del interprete de comandos, por defecto es el simbolo ">"
        self._usuario = usuario # Objeto usuario al cual este interprete atiende.
        
    def ayuda(self):
        """ 
        Este metodo imprime la ayuda del interprete de comandos, muestra una lista de comandos disponibles, asi como parametros que se pueden usar
        """
            
    
    def entrada(self, comando):
        """
        Comandos disponibles:
        
        """
        if len(comando) <= 0:
            return "Comando no encontrado o no existe"
        else:
            (comando, objeto, parametro) = _parseEntrada(comando)
            
    def _parseEntrada(self, com):
        comando, temp = com.split(" ",1)
        if comando.lower() not in COMANDOS_VALIDOS:
            return "Comando no encontrado o no existe"
        else:
            if comando == 'ingreso':
                u,c = temp.split(" ",1)
                autorizacion = Servidor.autoriza(u,c)  #Esto aun no existe, pero en este momento se llama al servidor para autenticar al usuario
                if autorizacion:
                    U.cambiaEstado('CONECTADO')
                else: return "Usuario o contrasenia incorrectos"
            elif comando == 'estado':
                accion = temp.lower()
                if  accion == 'estatus':
                    U.consultaEstado()
                elif accion in ['desconectado','ocupado','nodisponible']:
                    U.cambiaEstado(accion)
            elif comando == 'mensaje':
                destino,texto = temp.split(" ",1)
                try:
                    C.consultaContacto(destino)
                except:
                    
                usuarioDestino,mensaje = temp.split(':',1)
                self._usuario.enviaMensaje(Mensaje(mensaje,self._usuario,usuarioDestino))
                
            elif comando == 'contacto':
            
        
        
    def ingresoSistema(usuario, contrasena):

    def run(self):
        """
        Este sera el loop principal del interprete de comandos, basicamente es un loop infinito hasta que se da
        el comando de salida del sistema, de lo contrario, este seguira pidiendo comandos; en caso que algun comando
        falle o la entrada sea incorrecta, el sistema debe reportar el error, no abortarse y continuar con normalidad
        """

if __name__ == '__main__':
    interprete = Comandos(0)

    interprete.run()

        
        
        
        
