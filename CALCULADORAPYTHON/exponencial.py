import math
def funcion_exponencial(x):
    suma = 0.0


    for n in range(50+1):
        suma += math.pow(x,n)/math.factorial(n)
    return suma


print("valor es: ", funcion_exponencial(50))
print("Resultado es ", math.exp(50))