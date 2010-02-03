



import comun
import hashlib
from Contactos import Contactos

class ComandosError(Exception):
    def __init__(self,m):
        self.__mensaje = m
    
    def mensaje(self):
        return self.__mensaje
    
class Comandos:
    def __init__(self, modo, simbolo = "> "): 
        """
        Modo indicara si el interprete de comandos esta en modo interactivo o no
        """
        assert modo == 1 or modo == 0, "Modo de interprete de comandos incorrecto"  # 0: interactivo, 1: no interactivo
        _modo = modo
        _simbolo = simbolo # El indicador del interprete de comandos, por defecto es el simbolo ">" 
        
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
        if comando.lower() not in ['contacto','estado','mensaje','ingreso']:
            return "Comando no encontrado o no existe"
        else:
            if comando == 'ingreso':
                u,c = temp.split(" ",1)
                autorizacion = servidor.autoriza(u,c)  #Esto aun no existe, pero en este momento se llama al servidor para autenticar al usuario
                if autorizacion:
                    U.cambiaEstado('CONECTADO')
                else: return "Usuario o contrasenia incorrectos"
            elif comando == 'estado':
                if temp.lower() == 'estatus':
                    U.consultaEstado()
            elif comando == 'mensaje':
                
            elig comando == 'contacto':
            
        
        
    def ingresoSistema(usuario, contrasena):

    def run(self):
        """
        Este sera el loop principal del interprete de comandos, basicamente es un loop infinito hasta que se da
        el comando de salida del sistema, de lo contrario, este seguira pidiendo comandos; en caso que algun comando
        falle o la entrada sea incorrecta, el sistema debe reportar el error, no abortarse y continuar con normalidad

        """
 # FIXME
        
        
        
