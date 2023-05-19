mi_lista = [1,2,3]
tu_lista = (19,22,14)
su_lista = (33,34,63)
def multiplicar_por2(elemento):
    return elemento*2
def solo_impar(elemento):
    return elemento % 2 != 0
# Lista de pares de datos de las dos listas
print(list(zip(mi_lista,tu_lista,su_lista)))

una_lista = ["a","b","c","d","e","e","a"]
duplicados = set([x for x in una_lista if una_lista.coun(x) > 1])
print(duplicados)

# Expreción generadora
cuadrados = (x*x for x in range(5))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))

# Pasar una función generadora 
import math
print(sum(x*x for x in range(5)))

# Lista de comprehensión pasada como función
numeros_pares = [x for x in range(21) if x%2 == 0]
print([x for x in range(21) if x % 2 == 0])
print(numeros_pares)
