#Programa: Método de Punto Fijo
#Autor: Aguilar Ortiz Victor 
#Descripción: Resuelve ecuaciones algebraicas 
#             por el método de Punto Fijo
#Funnción con la que trabaja el progrma: 

import matplotlib.pyplot as plt
import math

ejex = []                                      #Lista donde se guardarán los valores del eje x
ejey = []                                      #Lista donde se guardarán los valores del eje y

print("Programa Metodo de Punto Fijo")
fgx = (input("Ingresa la funcion a utilizar en su forma g(x):"))
X0 = float(input("Ingresa el valor de X0:"))

erra = float(input("Ingresa el error permitido en porcentaje:"))
error = 10000
Xi_anterior = X0
n = 0

def f(x):                                  
    return eval(fgx, {"x": x, "e": math.e, "log": math.log, "sin": math.sin, "exp": math.exp})

while error > erra:
    Xi = f(X0)
    
    if Xi != 0:
        error = abs((Xi - Xi_anterior) / Xi) * 100
   
    Xi_anterior = Xi
    X0 = Xi
    
    n = n + 1                                  #Contador para n
    ejex.append(n)                             #Lista donde se guardarán los valores de n
    ejey.append(error)
    
plt.plot(ejex, ejey)                           #Creamos la gráfica
plt.title("Gráfica Para el Error Obtenido")    #Le damos nombre
plt.xlabel("Número de Repeticiones")           #Nombre eje x
plt.ylabel("Valores del Error")                #Nombre eje y
plt.show() 

print("La raiz es:", Xi)
print("Error aproximado en porcentaje es:", error)
  

