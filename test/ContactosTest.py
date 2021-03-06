#!/bin/usr/env python

#Importamos las librerias de Python
import unittest
import hashlib
import sys
sys.path.append("../src")

# Importamos nuestros archivos de mod
import Contactos
import comun


USUARIO = "fcodiaz"
CONTRASENA = "test123"


class ContactosTest(unittest.TestCase):
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
        
    def runTestDevuelveContactos(self):
        #C = Contactos.Contactos(self.userID)

        self.assertEqual(type(self.C.devuelveContactos()),type({}))
        
    def runAgregaContacto(self):
        #C = Contactos.Contactos(self.userID)
        self.C.agregaContacto(self.contactoID, self.contactoNombre, self.contactoEstado)
        self.assertEqual(self.C.consultaContacto(self.contactoID),(self.contactoID, self.contactoNombre))

        
    def runEliminaContacto(self):
        """
        Test eliminate a contact
        """
        #C = Contactos.Contactos(self.userID)
        self.C.agregaContacto(self.contactoID, self.contactoNombre, self.contactoEstado)
        self.C.eliminaContacto(self.contactoID)
        self.assertRaises(Contactos.ContactosError,self.C.consultaContacto,self.contactoID)        
        
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