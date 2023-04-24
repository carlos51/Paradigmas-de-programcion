from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario
#================================================
# Implementa la interface RepositorioDeUsuarios
#================================================
class SistemaDeArchivos(RepositorioUsuarios):
    __directorio: str

    def __init__(mi,directorio:str):
        mi.__directorio = directorio

    def abrir(mi) -> None:
        print(f"Abrir directorio: {mi.__directorio}")

    def guardar(mi,usuario:Usuario) -> None:
        xml = f"</root></name>{usuario.getNombre()}</neme></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root<"
        print(f"Guardado usuario en el archivo : {mi._directorio}/{usuario.getNombre()}"
        print(xml)

    def cerrar(mi) -> None:
        print("Cerrado")
