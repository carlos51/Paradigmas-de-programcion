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
comunicadores = MPI.COMM_WORLD

#=================================
# Numero total de procesos
#=============================
n_proceso = comunicadores.Get_size()

#====================================
# Numero identificador de este proceso
#====================================
quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso ",str(quien_soy),"de ", str(n_proceso))
