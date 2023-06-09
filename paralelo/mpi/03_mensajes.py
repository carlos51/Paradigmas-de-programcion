from mpi4py import MPI

#==================
# Objeto mensaje
#=================
class Mensaje:
    def __init__(self,rank):
        # iterador
        self.x = range(rank*10)
        # string
        self.p = "vengo del proceso "+ str(rank)

#======================
# Programa principal
#=====================
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)

    #======================================================
    # Que te mande el anterior y si es cero que sea el último
    #========================================================
    fuente = rank-1 if rank!=0 else size-1

    #=========================================================
    # Mándalo al siguiente y si eres el último mándalo al primero
    #============================================================
    destino = rank+1 if rank!=size-1 else 0

    #============================================================
    # send y recv son operaciones bloqueadas y generan que el
    # codigo se atore esprando que alguien reiciba un mensaje
    # esto se resuelve enviando con los pares y recibimos con
    # los impares
    #===========================================================

    # Si soy par
    if rank%2 == 0:
        #======================
        # Enviar mansaje s al dest
        #=========================
        comm.send(s, dest=destino)

        #=================================
        # Reicibir de source y lo pone en m
        #==================================
        m = comm.recv(source=fuente)
        comm.send(s,dest=destino)

    print("Soy el proceso ", rank, ", el resultado es ", len(m.x),",",m.p)
