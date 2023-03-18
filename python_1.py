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

