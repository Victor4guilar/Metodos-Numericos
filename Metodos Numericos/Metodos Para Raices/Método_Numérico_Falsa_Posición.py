#Programa: Método de Falsa Posición
#Autor: Aguilar Ortiz Victor 
#Descripción: Resuelve ecuaciones algebraicas 
#             por el método de Falsa Posición
#Funnción con la que trabaja el progrma: 

import matplotlib.pyplot as plt
import math
import sys

ejex = []                                      #Lista donde se guardarán los valores del eje x
ejey = []                                      #Lista donde se guardarán los valores del eje y

print("Programa Metodo de Falsa Posicion")
print("Ahora ingresa el intervalo")
Xa = float(input("Valor de Xa:"))
Xb = float(input("Valor de Xb:"))

erra = float(input("Ahora ingresa el error permitido en porcentaje:"))
error = 100
Xr = 0
Xrant = 0
e = math.e
n = 0

def f(x):                                  #Definimos la funcion f(x)
    return (e**-x) - x          #Escribimos la función para recibir los resultados de la funcion evaluada
#(e**-x)- math.log(x)
if (f(Xa) * f(Xb)) < 0:
    pass                                   #El código continúa con los siguientes pasos
else:
    print("La raiz no se encuentra dentro del intervalo")
    sys.exit()                             #Lo utilizamos para terminar el programa si la raiz no esta en ese intervalo.
    
while error > erra:
    funa = f(Xa)
    funb = f(Xb)
    Xr = Xa - ((funa * (Xb - Xa)) / (funb - funa)) #Calculamos el valor para Xr
    
    if Xrant != 0:                         #Solo calculamos el error si Xrant es diferente de 0
        error = abs((Xr - Xrant) / Xr) * 100 #Calculamos el error
    
    Xrant = Xr                             #Igualamos Xrant con Xr para poder calcular el error en la seguiente iteracion
    
    if (f(Xa) * f(Xr)) < 0:                #Evaluamos la primera condicion del metodo
        Xb = Xr                            
    elif (f(Xa) * f(Xr)) > 0:              #Evaluamos la segunda condicion del metodo
        Xa = Xr
    elif (f(Xa) * f(Xb)) == 0:             #Evaluamos la tercera condicion del metodo
        print("La raiz es:", Xr)
    else:                                  #Imprimimos error si no se cumple ninguna condicion
        print("Error-Raiz no encontrda")

    n = n + 1                                  #Contador para n
    ejex.append(n)                             #Lista donde se guardarán los valores de n
    ejey.append(error)
    
plt.plot(ejex, ejey)                           #Creamos la gráfica
plt.title("Gráfica Para el Error Obtenido")    #Le damos nombre
plt.xlabel("Número de Repeticiones")           #Nombre eje x
plt.ylabel("Valores del Error")                #Nombre eje y
plt.show() 

print("La raiz es:", Xr)
print("Error aproximado en porcentaje:", error)
     