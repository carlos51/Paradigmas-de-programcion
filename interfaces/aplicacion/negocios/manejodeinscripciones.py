from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorios.repositoriodeusuario import RepositorioDeUsuarios

#==========================
# Case storemanager
# NO TIENE VARIABLES!!!
#==========================
class ManejoDeInscripciones:
    #==================================================================
    # Decorador staticmethod
    # El objeto sólo tiene la función inscribirUsuario
    # ENVUELVE LA FUNCIUÓN SIN LLAMAR VARIABLES LOCALES
    # el objeto ManejoDeInscripciones es la interface intercambiable
    #==============================================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios)->None:
        print("-----------> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositoriDeUsuarios.cerrar()
