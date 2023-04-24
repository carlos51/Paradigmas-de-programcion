from aplicacion.repositorio.repositoriousuario import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#========================================
# S3 es hijo de RepositorioUsuarios
#=====================================
class S3(RepositorioDeUsuarios):
    __clinId: str
    __secretKey: str
    __bucket: str

    def __init__(mi, clientId: str, secretKey: str, bucket: str):
        mi.__clientId = clientId
        mi.__secretKey = secretkey
        mi.__bucket = bucket

    def abrir(mi) -> None:
        print(f"Estableciendo conexión a AWS S3 {mi.__clientId}:{mi.__secretKey}"

    def guardar(mi, usuario:Usuario) -> None:
        userData = {"nombre": usuario.getNombre(),
                    "apellido" : usuario.getApellido(),
                    "edad" : usuario.getEdad()}
        print(f"Guardando usuario de la bandeja: {mi.__bucket}: {userData}")

    def cerrar(mi) -> None:
        print("Cerrando coneción a AWS S3")

