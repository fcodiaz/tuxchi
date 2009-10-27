import unittest
import Contactos

import hashlib

USUARIO = "fcodiaz"
CONTRASENA = "test123"


class ContactosTest(unittest.TestCase):
    userID = hashlib.sha224(USUARIO)
    passwd = hashlib.sha224(CONTRASENA)    
    
    contactoID = hashlib.sha224("foo")
    contactoNombre = "Usuario Foo"
    contactoEstado = 0
    
    def setUp(self):
        print "Setup call"


        
        
    def tearDown(self):
        print "Tear Down call"
        
    def runTestDuenoContactos(self):
        C = Contactos.Contactos(self.userID)

        self.assertEqual(C.duenoContactos(),self.userID)
        
    def runTestDevuelveContactos(self):
        C = Contactos.Contactos(self.userID)

        self.assertEqual(type(C.devuelveContactos()),type({}))
        
    def runAgregaContacto(self):
        C = Contactos.Contactos(self.userID)
        C.agregaContacto(self.contactoID, self.contactoNombre, self.contactoEstado)
        self.assertEqual(C.consultaContacto(self.contactoID),(seld.contactoID, self.contactoNombre))

        
    def runCreaContacto(self):
        """
        Test some 
        """
        
    def runEliminaContacto(self):
        """
        Test eliminate a contact
        """
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ContactosTest("runTestDuenoContactos"))
    suite.addTest(ContactosTest("runTestDevuelveContactos"))
    suite.addTest(ContactosTest("runAgregaContacto"))
    #suite.addTest(ContactosTest("runCreaContacto"))
    #suite.addTest(ContactosTest("runEliminaContacto"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)