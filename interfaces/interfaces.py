#======================================================================================0
# Del directorio aplicación, el subdirectorio repositorio.
# el archivo basededatos.py : traer el objeto Base de datos
#==========================================================
from aplicacion.repositorio.basededatos import BaseDeDatos

#==========================================================
# Del derectorio aplicación, subdirectorio repositorio,
# el archivo s3.py : traer el objeto s3
#========================================================
from aplicacion.repositorio.s3 import S3

#=======================================================00
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo sistemadearchivos.py : traer el objeto SistemaDeArchivos
#=====================================================================
from aplicacion.repositorio.sistemasdearchivos import SistemasSeArchivos

#================================================================
# De directorio aplicacion, el subdirectorio modelos,
# el archivo usuario.py : traer el objeto Usuario
#=============================================================
from aplicacion.modelos.usuario import Usuario

#=================================================
# Del derectorio aplicacion, el subdirectorio negocion,
# el archivo manejodeindcriopciones.py : traer el objeto ManejoDeInscripciones
#=============================================================================
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

#=========================
# Crear el objeto Usuario
#=========================
usuario = Usuario("Roberto","Jimenez",18)

#=======================================
# Crear el objeto s3
#======================
repositoriosS3 = S3("234724291","sdf223434","MiCuenta")

#========================================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#================================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#============================================
# Crear el objeto sistemadearchivos
#===========================================
repositorioSistemaDeArchivos = SistemaDeArchivos("home/users")

#==========================================================
# Interface inscribirUsuario del onjeto ManejoDeInscripcones
#==========================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#=========================
# Crar el objeto basededatos
#============================
repositorioBaseDeDatos = BaseDeDatos("lical","admin","admin123")

#========================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")


