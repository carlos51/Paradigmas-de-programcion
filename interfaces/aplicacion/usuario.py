#=========================
# Clase Usuario
#====================
class Usuario:
    __nombre:str
    __apellido:str
    __edad:str

    #===========
    # Constructor
    #============
    def __init__(mi,nombre: str, apellido:str, edad:str):
        mi.__nombre = nombre
        mi.__apellido = apellido
        mo.__edad = edad


    #=========
    # Getters
    #========
    def getNombre(mi)->str:
        return mi.__nombre

    def getApellido(mi)->str:
        return mi.__apellido
    def getEdad
