#=============
# Uso de filtros
#==============

#================================================================00
# Hacer una lista de los números por arriba del promedio
#=======================================================

# Módulo de estadística
import statics

bigdata = [1.23,23.23,34.3,24.33]
promedio = statics.mean(bigdata)
print(promedio)

#==============
# Limpiar los datos
#==================
paises = ["","Argentina","","Brasil","","Chile","México","","Colombia","","","Cuba","Venezuela"]

#========================================
# Filtra lo que no contiene nada
#========================================
print(list(filter(None,paises)))
