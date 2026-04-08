#Programa: Método de la Secante
#Autor: Aguilar Ortiz Victor 
#Descripción: Resuelve ecuaciones algebraicas 
#             por el método de la Secante 
#Funnción con la que trabaja el progrma: 

import matplotlib.pyplot as plt
import math

ejex = []                                      #Lista donde se guardarán los valores del eje x
ejey = []                                      #Lista donde se guardarán los valores del eje y

print("Programa Metodo de la Secante")
fun = (input("Ahora ingresa la funcion a utilizar:"))
X0 = float(input("Ingresa el valor de X0:"))
X1 = float(input("Ingresa el Valor de X1:"))

erra = float(input("Ahora ingresa el error permitido en porcentaje:"))
error = 10000
Xi_anterior = X1
n = 0

def f(x):                                  
    return eval(fun, {"x": x, "e": math.e, "log": math.log, "sin": math.sin, "exp": math.exp})

while error > erra:
    fx1 = f(X1)
    fx0 = f(X0)
    
    Xi = X1 - (((fx1) * (X0 - X1)) / ((fx0) - (fx1)))
    
    if Xi != 0:
        error = abs((Xi - Xi_anterior) / Xi) * 100
   
    Xi_anterior = Xi
    X1 = Xi
    
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
    
    
