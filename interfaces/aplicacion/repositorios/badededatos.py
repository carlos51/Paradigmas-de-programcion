from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuarios import Usuario

#=========================================================
# Para llenar la interfave hay que heradar la clade
#=====================================================
class BadeDeDatos(RepositorioDeUsuarios):
    __host: str
    __user: str
    __password: str

    def __init(mi,host:str, user:str, password:str):
        mi.__host = host
        mi.__user = user
        mi.__password = password

    def abrir(mi) -> None:
        print(f"Abriendo la coneción a la base de datos: {mi.__host}:{mi.__user}@{mi.__password}")

    def guardar(mi, usuaro:Usuario) -> None:
        userElements = {"nombre": usuario.getNombre(),
                        "apellido": usuario.getApellido(),
                        "edad" : usuario.getEdad()}
        print(f"
