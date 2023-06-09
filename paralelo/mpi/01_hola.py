#==================================================
# mpiexec -n 4 python3 hola_mpi.py
# mpirun -n 4 python3 hola_mpi.py
#=======================================
# Para corrar en 4 procesos
#============================
from mpi4py import MPI

#================================
# Crear un pbjeto comunicador
#===============================
comucicadores = MPI.COM_WOLD

#=================================
# Numero total de procesos
#=============================
n_procesos = comunicadores.Get_size()

#====================================
# Numero identificador de este proceso
#====================================
quien_soy = comunicadorese.Get_rank()

print("Saludos desde el proceso ",str(quien_soy),"de ", str(n_proceso))
