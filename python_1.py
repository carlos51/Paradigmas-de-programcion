#===================
# Operaciones básicas
#====================
print(2+3)
print(2*3)
print(2/3)
print(2**10)
print(2**0.5) #raíz cuadrada
print(10%2)
print(10%0.1)

#====================================
# Para saber el tipo de objeto se usa type
#=========================================
t=0
print(type(t)) #entero
t=3.1
print(type(t)) #boleano (bool)
t=True
print(type(t)) #boleano (bool)

#=====================
# Mensa a pantalla
#=================
print("Este es un comando de python." , "Este es otro enunciado.",t)
print('id: , 1')
print('First Name: ', 'Steve')
print('last Name: ', 'Jobs')
print("vamos a sumar esto" , " con esto otro")

#==============================================
# Continuar una instrucción en varios renglones
#==============================================
if 100 > 99 and\
    200 <= and \
    True != False:
        print('Hello Worols')

#===============================================
# Comandos diferentes en la misma línea
#======================================
print("Hola "); print("tu!!") #Se considera mala práctica

#======================================================
# Usando paréntesis redondos, cuadrados o llaves
# se puede escribir en varios renglones
#=================================================
list = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]
matriz = [[1,2,3,4],[5,6,7,8],[9,19,11,12]]

print(list)
print(matriz)

#==================================================================
# Indentacjión estricta para procesos dependientes de : (dis puntos)
#===================================================================
if 10>5:
    print("diez es mayor que cinco")
    print("otra identacion")
for u i in list:
    print(i)
    print("ok")
if 10>5:
    print("verdadero")
    if 10<20:
        print("verdadero")
elif 5>3:
    print("esto no se imprimirá")
else:
    print("aqui llega")
#================
# Funciones
#==========
def say_hello(name):
    print("Hello ", name)
    print("Welcome to Python Tutorials")
#=========================================
# Inptut permite obtener datos del usuario en promter
#====================================================
nombre = input("Dame tu nombre: ")
print("Hola como estás ", nombre)

#========================================
# Los enteros son de precición ilimitada
#=======================================
y = 5000000000000000000000000000000000
print(y)

#================================
# Se puede delimitar números con un guión bajo pero no con coma
#==============================================================
y = 5_000_000
print(y)

#======================================================
# La función int() cambia strings y flotantes a enteros
#======================================================
numero = int(input("Dame tu edad "))
type(numero)

#========================================================
# La notación científica de flotantes utiliza e o E
#===================================================
# 1.2 x 10^{.4}
#==============
y = 1.2E-09
print(y)

#=======================================================
# La función float() convierte strings y enteros a floats
#========================================================
y = float("14.3")
print(y)

#========================================================
# Los complejos se escriben con la raíz de menos una
# j siempre con un número como prefijo
# no acepta la j suelta
#=======================================================
z = 1+1j

# suma +
# resta -
# multiplicación *
A# división /
# exponente **
# // función piso
# Funciones para transformar numeros int() complex()
# Operaciones abs() round() pow()

print(round(314159,4)

#===========================
# Strings de varias líneas
#==========================
pararrafo = """ En el bosqu de la china
la chinita se perdió"""
print(parrafo)

#=========================================
# La función len() obtiene el tamaño del string
#==============================================
n = len(parrafo)
print(n)

#================================================
# KLas letras en un string ocupan lugares como en un arreglo 
# (tambien de atrás para adelante comenzando en -1 el último)
#============================================================
palabra = "hola"
print(parabra[0])
print(palabra[-4])

#==============================================
# Convertir secuencia a conjunto
# No lo genera en ordeb
#===============================================

s = set("Hello")
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

su = s1|s1 # Union
print(su)

si = s1&s2 # Interseccion
print(si)

#================================
}# Uso de diccionarios
#===============================
capitals = {"USA":"Washington","France":"Paris","India":"New Delhi"}
print(capitals)

#=================================
# llave:valor 
#===============================
# Diccionario vacio
d = {}

# Llave entrada, valor string
nunNames = {1:"One",2:"Tow", 3:"Tree"}

# Llave real, valor string
decNames = {1.5:"One and Half",2.5:"Two and Half",3.5:"Three and Half"}

# Llave tupla, valor string
items = {("Parquer","Reynols","Camlin"):"pen",("LH", "Wirpool","Samsung"):"Refrigerador"}

# Llave string, valor int
romanNums = {"I":1, "II":2, "III":3, "IV":4, "V":5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("india"))

# Reportar llave y valor
for k in capitals:
    print("Key = " + k + " , Value = " + capitals[k])

# Nuevo dato para el diccionario
del capitals["Mexico"]
print(capitals)

# Borrar todo el diccionario
del capitals

# Reportar llaves
print(roamanNums.keys())

# Reportar valores
print(romanNums.vakues())

# Juicio de llaves (está o no está llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)


#=====================================
# Listas
# Las listas pueden ser de objetos diferentes
#==============================================
miprimeralista = [] # Lista vaciá
print(miprimeralista)

#=============================================
# list: hacer una lista
# range(i,j): secuencia de i hasta j-1
#==========================================

nums = list(ran
