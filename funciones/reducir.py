#================================
# Uso de reduciones (colapsar resultados)
#=========================================

#============================================0
# Multiplicación de todos los numeros en la lesta
#================================================

from functool import reduce

bigdata = [2,4,5,6,7,8,9,345,4,353]

#===============
# Función x*y
#==============
multiplicar = lambda x,y:x*y

print(reduce(multiplicar,bigdata))

#========================================================0
# Reduce le aplica la función por pares a los resultados y
# el siguiente elemento comenzando con los dos primeros
# elementos
#==========================================================

