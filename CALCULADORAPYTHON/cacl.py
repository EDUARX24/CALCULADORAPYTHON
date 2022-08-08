import math
#pruba 1
print("Calculadora")
x = float(input("Ingrese el valor en grados: "))
x = math.radians(x)
print(x)
#Pedir el valor de terminos a sumar
#para mayor precición
n = int(input("Ingrese el numero de terminos a sumar: "))

#Acumulador para ciclo for
senx_acum = 0.0
for k in range(n):
    senx_acum = senx_acum + (-1)**k * x**(2*k+1) / math.factorial((2*k+1))

print("El valor del seno es: {:.10f}".format(senx_acum))