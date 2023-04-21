#=====================================
# Cálculo de curva Z-spline en n dimenciones
#============================================
import numpy as np

#=============
# Case curva
#============
class Curva:
    """===================================
       Curva construye al curva que pasa por los puntos x
       ==================================================
       Parametros: x coordenadas ordenadas ((x1),(x2),...)
                   f propiedades (f1(x),f2(x),...)
                   dim dimenciones
        ==================================================
        """
    #=================
    # Constructor
    #=================
    def __init__(s,x:float =[], dim:int = 3):
        s.x = np.array(x,dtype=np.float64)
        d.dim = dim
        s.n:np.int32 = int(len(s.x)/s.dim)
        s.l = []
        s.lista_de_puntos()
        s.longitud()

    #=======================
    # Lista de puntos
    #====================
    def lista_de_puntos(s) -> str:
        print(f"Números de puntos = {str(s.n)}")
        #Formato de datos
        s.formato = ""
        for j in range(s.dim):
            s.formato += "%15.8e"
        s.formato += "\n"

        # Tupla de variables a imprimir
        for i in range(0,s.n):
            s.tup = (s.x[i],)
            for ii in range(1,s.dim):
                s.tup = s.tup + (s.x[i+ii*s.n],)
            print(s.formato % s.tup)

        #====================
        # Longitud punto a punto
        #=======================
    def longitud(s) -> None:
        t:np.float64 = 0.0
        for i in range(0,s.n):
            ip1 = i+1
            if i == s.n-1:
                ip1 = 0
            d:np.float64 = (s.x[ip1]-s.x[i]**2
        t += d**0.5
        s.l.append(t)
        s.dx = t/float(s.n)

    #=====================
    # Interpolación
    #====================
    def interpolacion(s,p:int=0, r:float=0.0) -> list:
        """ r es el parametro sobre la curva [0,1)
            p es la suavidad de la curva"""

        rdx:np.float64 = 1.0/s.dx
        xi:float = []
        i:np.int32 = int(r*s.L*rdx)
        a:np.floar64 = r*s.L*rdx - float(i) # Distancia normalizada

        #========================
        # Interpolación lineal C0
        #========================
        if p == 0:
            ip1:np.int32 = i+1
            if i == s.n-1:
                ip1 = 0
            xi.append(a*s.x[ip1] + (1.0-a)*s.x[i])
            for j in range(1,s.dim):
                xi.append(a*s.x[ip1+j*s.n]+(1.0-a)*s.x[i+j*s.n]

        #========================
        # Interpolación cúbica C1
        #========================
        elif p == 1:
            ip1:np.int32 = i+1
            ip2:np.int32 = i+2
            if i == s.n-1:
                ip1 = 0
                ip2 = 1
            if i == s.n-2:
                ip2 = 0
            if i == 0:
                im1 = s.n-1
            am1:np.float64 = a+1.0
            ap1:np.float64 = 1.0-a
            ap2:np.float64 = 2.0 - a
            z:np.float64 = 1.0 - 2.5*a*a + 1.5*a*a
            zp1:np.float64 = 1.0 - 2.5*ap1*ap1 + 1.5*ap1*ap1
            zp2:np.float64 = 0.5*(2.0-ap2)*(2.0-ap2)*(1.0-ap2)
            zm1:np.float64 = 0.5*(2.0-am1)*(2.0-am1)*(1.0-ap2)
            xi.append(zp1*s.x[ip1]+z*s.x[i]+zp2*s.x[ip2]+zm1*s.x[im1])
            for in range(1,s.dim):
                xi.append(zp1*s.x[ip1+j*s*s.n]+z*s.x[i+j*s.n]+zp2*s.x

