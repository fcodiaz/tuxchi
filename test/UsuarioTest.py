#!/bin/usr/env python

#Importamos las librerias de Python
import unittest
import hashlib
import sys
sys.path.append("../src")

# Importamos nuestros archivos de mod
import Usuario
import comun


USUARIO = "fcodiaz"
CONTRASENA = "test123"


class UsuarioTest(unittest.TestCase):
    userID = hashlib.sha224(USUARIO)
    passwd = hashlib.sha224(CONTRASENA)    

    
    def setUp(self):
        print "Setup call"
            
        self.contactoID = hashlib.sha224("foo")
        self.contactoNombre = "Usuario Foo"
        self.contactoEstado = 0
        
        self.C=Contactos.Contactos(self.userID)        
        
    def tearDown(self):
        print "Tear Down call"
        self.C.destruyeContactos()
        
    def runTestDuenoContactos(self):
        #C = Contactos.Contactos(self.userID)

        self.assertEqual(self.C.duenoContactos(),self.userID)
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ContactosTest("runTestDuenoContactos"))
    suite.addTest(ContactosTest("runTestDevuelveContactos"))
    suite.addTest(ContactosTest("runAgregaContacto"))
    suite.addTest(ContactosTest("runEliminaContacto"))
    #suite.addTest(ContactosTest("runCreaContacto"))
    #suite.addTest(ContactosTest("runEliminaContacto"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite) 