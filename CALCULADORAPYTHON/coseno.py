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
cose_acum = 0.0
for k in range(n):
    cose_acum = cose_acum + (-1)**k * x**(2*k) / math.factorial((2*k))

print("Coseno del numero es:  {:.10f}".format(cose_acum))