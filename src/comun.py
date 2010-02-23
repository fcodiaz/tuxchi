import pickle

# Constantes del sistema

# Parametros del sistema

__VERSION__ = "0.0.1"
__NOMBRE__ = "tuxchi"   #http://www.sepomexyuc.gob.mx/prehisp.html

PARAM = {"puerto":12345, \
        "version":__VERSION__,\
        "dirusuario":"."+__NOMBRE__,\
        "configuracion":"."+__NOMBRE__+"/config",\
        "imagenes":"."+__NOMBRE__+"/imagenes/"
        }
        

# Estados del Usuario
ESTADOS=(DESCONECTADO, CONECTADO, OCUPADO, AUSENTE, INVISIBLE, NOMOLESTAR) = (0, 1, 2, 3, 4, 5)

def serialize(obj):
    return pickle.dumps(m)

def unserialize(str):
    return pickle.loads(str)