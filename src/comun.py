

# Constantes del sistema

# Parametros del sistema

__VERSION__ = "0.0.1"
__NOMBRE__ = "tuxchi"   #http://www.sepomexyuc.gob.mx/prehisp.html

PARAM = {"puerto":12345, \
        "version":__VERSION__,\
        "configuracion":"/etc/"+__NOMBRE__
        
        }
        

# Estados del Usuario
(DESCONECTADO, CONECTADO, OCUPADO, AUSENTE, INVISIBLE, NOMOLESTAR) = (0, 1, 2, 3, 4, 5)
