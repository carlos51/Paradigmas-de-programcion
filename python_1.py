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
if 100 > 99 and True != False:
        print('Hello Worols')

#===============================================
# Comandos diferentes en la misma línea
#======================================
print("Hola "); print("tu!!") #Se considera mala práctica

#======================================================
# Usando paréntesis redondos, cuadrados o llaves
# se puede escribir en varios renglones
#=================================================
lista = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]
matriz = [[1,2,3,4],[5,6,7,8],[9,19,11,12]]

print(lista)
print(matriz)

#==================================================================
# Indentacjión estricta para procesos dependientes de : (dis puntos)
#===================================================================
if 10>5:
    print("diez es mayor que cinco")
    print("otra identacion")
for i in lista:
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
# división /
# exponente **
# // función piso
# Funciones para transformar numeros int() complex()
# Operaciones abs() round() pow()

print(round(314159,4))

#===========================
# Strings de varias líneas
#==========================
#parrafo = "En el bosqu de la china la chinita se perdió"
#print(parrafo)

#=========================================
# La función len() obtiene el tamaño del string
#=============================================
#texto = "texto"
#n = len(texto)
#print(n)

#================================================
# KLas letras en un string ocupan lugares como en un arreglo 
# (tambien de atrás para adelante comenzando en -1 el último)
#============================================================
palabra = 'hola'
print(palabra[0])
print(palabra[-4])

#==============================================
# Convertir secuencia a conjunto
# No lo genera en ordeb
#===============================================

s = set("Hello")
print(s)

s.add(100)
print(s)

#s.update(nums)
#print(s)

s.remove(100)
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

su = s1|s1 # Union
print(su)

si = s1&s2 # Interseccion
print(si)

#================================
# Uso de diccionarios
#===============================
capitals = {"USA":"Washington","France":"Paris","India":"New Delhi","Mexico":"CDMX"}
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
print(romanNums.keys())

# Reportar valores
print(romanNums.values())

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

nums = list(range(1,61))

for i in nums:
    print(i)

#===================================
# Incluir nuevos elementos en la lista
#=====================================

nums.append(61)
nums.append(62)
nums.append(61)
print(nums)

#================================
# Borrar lista
#=========================
del nums

#================================
# Sumar listas
#=============================0
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

#==============================
 # Llenado a mano
#========================00
potencial = []
for i in range(0,1000):
    potencial.append(float(i))
print(potencial)

potencial = tuple(potencial)
print(potencial)

#==============================0
# Condicionales 
#================================
precio = 50
#................
# Si esto....
#...........
if precio < 50:
    print("El precio es menor que 50")
#...........
# Se no ... si esto otro...
#.....................
elif precio > 50: 
    print("El preicio es mayor a 50")
#...................
# se nada de lo anterior....
#........................
else:
    print("El precio es 50")

precio = 50 
cantidad = 5
total = precio*cantidad
#===============================
# Condicionales anidados
#=0=============================
if total > 100:
    if total > 500:
        print("Total es mayor que 500")
    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 pero mayor que 400")
        elif total < 500 and total > 300:
            print("Total entre 300 y 500")
        else:
            print("Total entre 100 y 300")
                
#================================
# Contador mientras la condición dea verdadera
#=============================================
num = 0
while num < 5:
    num = num + 1
    print("num = " , num)

num = 0
#=====================
# Primera funcion
#=====================
def saludo():
    #=====================
    # Documentación rápida de la funcuón 
    #===================================
    """Esta funcion saluda"""
    print("!Quiúboles!. ¿como estas?")

#====================================
# Llamando de la funcuón
#=================================
saludo()

#==================================
# Se ejecuta pero no se asigna
#================================
salida = saludo()

#==========================
# Esto no funciona
#=========================
print(salida)

#========================
# Mostrar documentación
#=======================0
# help(saludo)

#=========================
# Función con argumento
#========================

def salu2(nombre):
    """Esta función te saluda por tu nombre"""
    print("Que onda ese ", nombre, "!")
salu2("Angel")
salu2("Julian")

#========================================
# Ahorrar trabajo del intérprete
# nombre:str la variable nombre es un str
#========================================
def saludos(nombre:str):
    """Esta función te saluda por tu nombre estrictamente"""
    print("Que onda ese ",nombre, "!")
saludos("Julian")
a = 123
print(type((a)))
saludos(a)

#==================================
# Función con muchos argumentos
#================================
def saludos_multiples(nombre1, nombre2, nombre3):
    """Esta función saluda a 3 personas al mismo tiempo"""
    print("Hola ", nombre1, ",", nombre2, ",", nombre3)
saludos_multiples("Hugo", "Juan", "Paco")

#=============================
# Bucle sobre lista
#===========================
nums = [10, 20 , 30, 40, 50]
for i in nums:
    print(i)

#===============================
# Bucle sobre un diccionario
# Items = elementos
#================================

numsNames = {1:"One", 2:"Two", 3: "Three"}
for pair in numsNames.items():
    print(pair)
#=========================================
# Bucle sobre diccionario
# key = llave
# value = valor
#========================================
for k,v, in numsNames.items():
    print("key = ", k, " value =",v)

#============================
# Primera funcuón
#==========================
def saludo():
    #=========================
    # Documentacion rápida de la dunción
    #==================================
    """ Esta función sauda"""
    print("¡Quiuboles!, como estas")

#=======================
# Llamado de la funcion
#=======================
saludo()

#========================
# Se ejecuta pero no se signa
#============================
salida = saludo()

#==========================
# Esto no funciona
#=======================
print(salida)

#==========================
# Mostrar documentación
#==========================
#help(saludo)

#============================
# Función ocn argumento
#=========================
def salu2(nonbre):
    """Esta función te saluda por tu nombre"""
    print("que onda ese", nombre, "!")
#=========================================
# Ahorrar trabajo del intérprete
# nombre:str la variable nemvre es un str
#===========================================
def saludos(nombre:str):
    """Esta función ter saluda por tu nombre estrictamente"""
    print("que onda ese", nombre, "!")
saludos("Julian")
a = 123
print(type(a))
saludos(a)

#=======================================
# Función con muchos argumentos
#=======================================
def saludos_multiples(nombre1, nombre2, nombre3):
    """Esta función saluda a 3 personas al mismo tiempo"""
    print("Hola ", nombre1, ",",nombre2, ",", nombre3)
saludos_multiples("Hugo", "Paco", "Luis")

#===================================================
# Función con cualquier número de argumentos
#==================================================
def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i = 0
    #===========================================0
    # end= es para ponerlo de corrido
    #============================================
    print("Hola ", end="")
    while len(nombres)<i:
        #Ultimo nombre
        if(i==len(nombres)-1):
            print(nombres[i])
        else:
        #Cualquier otro nombre
            print(nombres[i], end=",")
        i+=1

muchos_saludos("Bosco", "Angel", "David", "Tamra", "Milli", "Edwin", "Lev","Luis","Abigail")
def greet(firstname, lastname):
    print("Hello", firstname, lastname)

#================================================================
# Lamar la función con argumentos en desorden
#============================================
greet(lastname="Jobs", firstname="Stebve")

#======================
# Función con valores por defecto
#==============================
def greet(**person):
    #================================
    # persona tiene caracteristicas firstname y lastname
    #======================================================
    print("Hello ", person["firstname"], person["lastname"])

greet(firstname= "Steve", lastname= "Jobs")
greet(lastname="Jobs", firstname="Steve")
greet(firstname="Bill", lastname="Gates", age=55) # Se pueden pasar más parametros de los necesarios

#======================================
# Función con valores por defecto
#=====================================
def greet(name = "Guest"):
    print("Hello", name)

greet()
greet("Steve")

#===============================
# Función con resultados
#==============================
def suma(a,b):
    return a + b

#==============================
# Programación funcional
# Se pueden en funciones en funciones
#====================================
total = suma(5, suma(10, 20))
print(total)

#===================================
# Cálculo lambda
# nombre de la función = lambda variable : función
#=================================================
x_al_cuadrado = lambda x : x * x
a1 = x_al_cuadrado(5)
print(a)

#======================================
# Lambda de varias variables
#================================
suma = lambda x1, x2,x3 : x1+x2+x3
print(suma(99,98, 97))

#===============================
# Uso de un función anónima
# El argumento va fuera entre paréntesis
#=======================================
print((lambda x : x*x)(6)) # Función anónima

#===================================
# Función con variable global
# EVITE EL EXESO !!!!!!!!!!!!!!!!
#===================================
name = "Steve"
def greet():
    global name #Para utilizar una variable global (que viene de fuera del bloque)
    name = "Bill"
    print("Hello ", name)

greet()

#==============================
# PROGRAMCIÓN ORIENTADA A OBJETOS
#=================================

#==================================
# Una clase para un objeto vacío
# No está tan vacío, necesita
# la palabra pass = pasar
#====================================
class ObjetoVacio:
    pass

#===============================
# nada es un OvjetoVacio
#============================
nada = ObjetoVacio()
print(type(nada))

#================================
# La clase llanta
#================================
class Llanta:
    #====================================
    # Variable cuenta es de toda la clase
    #====================================
    cuenta = 0
    #=====================================
    # Función constructora de identidad
    # __init__ es una función reservada
    # comienza con uno mismo: self
    # pero puede ser otro nombre (mi)
    # parámetros de entrada = default
    #======================================
    def __init__(mi, radio=50, ancho=30, presion=1.5):
        #variable de la estructura conpleta Llanta
        Llanta.cuenta +=1
        # variables exclusivas de cada objeto+
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion

#==========================
# Objetos (instanciados)
#=========================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40, 30, 1.6)

#==================================
# Objeto que contiene otros objetos
#==================================
class Coche:
    def __init__(self, ll1, ll2, ll3, ll4):
        self.llanta = ll1
        self.llanta2 = ll2
        self.llanta3 = ll3

micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ", Llanta.cuenta) # Variable global de la clase
print("Presión de llanta 4 = ", llanta4.radio)
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de llanta 3 =", llanta3.radio)
print("Presión de la llanta 1 de mi coche = ", micoche.llanta.presion)

#=====================================
# Encapsulamiento
#==============================

#============================
# Uso de la funcón de python property para poner y obtener atributos
#===================================================================
class Estudiante:
    def __init__(self):
        self.__nombre = ""
    def ponerme_nombre(self, nombre):
        print("se llamó a ponerme_nombre")
        self.__nombre = nombre
    def obtener_nombre(self):
        print("se llamó a obtener_nombre")
        return self.__nombre
    nombre = property(obtener_nombre, ponerme_nombre)

#============================================00
# Crear objeto estudianate sin nombre
#====================================
estudiante = Estudiante()

#========================================================0
# Ponerle nombre usando la propiedad nombre y el método ponerme_nombre
# (sin tener que llamar explícitamente la función)
#=====================================================================
estudiante.nombre = "Diego"

#================================================================
# Obtener el nombre con el método obtener_nombre
# __nombre es una variable encapsulada (no visible desde fuera)
# (sin tener que llamar explícitamente a la fución obtener_nombre)
#================================================================
print(estudiante.nombre)

# Esto no funciona
# print(estudiante.__nombre)

#================================
# Herencia de clases
#====================
class Cuadrilatero:
    def __init__(self, a, b, c, d):
        self.lado1 = a
        self.lado2 = b
        self.lado3 = c
        self.lado4 = d

    def perimetro(self):
        p = self.lado1 + self.lado2 + self.lado3 + self.lado4
        print("perimetro = ", p)
        return p

#================================================
# Su hijo rectángulo
# Rectángulo es hijo de Cuadrilátero
# Rectángulo (Cuadrilateroo)
#===============================================
class Rectangulo(Cuadrilatero):
    def __init__(self,a,b):
        #==============================
        # Constructor se su madre
        #==============================
        super().__init__(a,b,a,b)

#==============================
# Su nieto Cuadrado
# Hijo de Rectángulo
#=============================
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)
    def area (self):
        area = self.lado1**2
        return area

    def perimetro(self):
        p = 4 * self.lado1
        print("perimetro = ", p)
        return p

#=============================
# Crear un cuadra
#============================
cuadrilatero1 = Cuadrilatero(1,2,3,4)
cuadrado = Cuadrado(5)

#========================================================0
# Llamar al método perímetro de su abuelo Cuadrilatero
#=======================================================
perimetro1 = cuadrilatero1.perimetro()

#===================================================
# Llamar a su propio método área
#==================================================
area1 = cuadrado.area()

print("Perímetro = ", perimetro1)
print("Area = ", area1)

#===================================
# Sobre-escribrir un método de su madre o abuela o tatarabuela...
# Es volver a definir una función ya existente
#================================================================

#=======================================================
# La clase A tine tres números reales
#=====================================================
class A:
    __a:float = 0.0
    __b:float = 0.0
    __c:float = 0.0

    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

#=======================================================
# La clase B tiene dos números reales
#========================================================
class B:
    __d:float = 0.0
    __e:float = 0.0
    def __init__(self,d:float, e:float):
        self.d = d
        self.e = e

    #================================================
    # Método sumar todo (internos + externos)
    #===============================================
    def sumar_todo(self, aa:float, bb:float):
        x:float = self.d + self.e + aa + bb
        return x
#===============================================
# ASOCIACIÓN
#=================================0
#Usando objetos independientes
objetoA = A(1.0, 2.0, 3.0)
objetoB = B(4.0, 5.0)
print(objetoB.sumar_todo(objetoA.a,objetoA.b))

#==========================================
# El objeto C tiene dos reales y un objeto A
# El objeto A se instancia dentro de C
#============================================
class C:
    __d:float = 0.0
    __r:float = 0.0
    __Aa:A= None

    def __init__(self, d:float, e:float):
        self.d = d
        self.e = e
        # A está instanciado adentro
        self.Aa = A(1.0,2.0,3.0)

    def sumar_todo(self):
        x:float = self.d + self.e + self.Aa.a + self.Aa.b
        return x

#=============================
# COMPOSICIÓN
# Contiene otro objeto dentro
#============================
objetoC = C(4.0, 5.0)
print(objetoC.sumar_todo())

#=====================================
# Objeto D tene dos reales y un objeto A
# definido por fuera
#=======================================
class D:
    __d:float = 0.0
    __Aa:A=None
    
    def __init__(self, d:float, e:float, Aa:A):
        self.d = d
        self.e = e
        self.Aa = Aa

    def sumar_todo(self):
        x:float = self.d + self.e + self.Aa.a + self.Aa.b
        return x

#====================================
# AGREGACIÓN
# Construye el objeto agregado por fuera
#=======================================
objetoD = D(4.0, 5.0, objetoA)
print(objetoD.sumar_todo())

