#Programa: Método de Newton-Raphson
#Autor: Aguilar Ortiz Victor 
#Descripción: Resuelve ecuaciones algebraicas 
#             por el método de Newton-Raphson
#Funnción con la que trabaja el progrma: 

import matplotlib.pyplot as plt
import math

ejex = []                                      #Lista donde se guardarán los valores del eje x
ejey = []                                      #Lista donde se guardarán los valores del eje y

print("Programa Metodo de Newton-Raphson")
fun = (input("Ahora ingresa la funcion a utilizar:"))
fprima = (input("Ahora ingresa su derivada:"))
Xi = float(input("Ingresa el Valor Inicial:"))

erra = float(input("Ahora ingresa el error permitido:"))
error = 10000
Xn = 0
Xn_anterior = Xi
n = 0

def f(x):                                  
    return eval(fun, {"x": x, "e": math.e, "log": math.log, "sin": math.sin, "exp": math.exp})

def g(x):                                  
    return eval(fprima, {"x": x, "e": math.e, "log": math.log, "sin": math.sin, "exp": math.exp})

while error > erra:
    fxi = f(Xi)
    fpxi = g(Xi)
    
    Xn = Xi - ((fxi) / (fpxi))
  
    if Xn != 0:
        error = abs((Xn - Xn_anterior) / Xn)
   
    Xn_anterior = Xn
    Xi = Xn
    
    n = n + 1                                  #Contador para n
    ejex.append(n)                             #Lista donde se guardarán los valores de n
    ejey.append(error)
    
plt.plot(ejex, ejey)                           #Creamos la gráfica
plt.title("Gráfica Para el Error Obtenido")    #Le damos nombre
plt.xlabel("Número de Repeticiones")           #Nombre eje x
plt.ylabel("Valores del Error")                #Nombre eje y
plt.show() 

print("La raiz es:", Xn)
print("Error aproximado es:", error)
