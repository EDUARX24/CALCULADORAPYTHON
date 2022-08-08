#the last dance
import math
# import msvcrt

# print("Presione una tecla para continuar...")
# msvcrt.getch()

def FuncionSeno():
    while True:
        
        try:
            print("Calculadora")
            x = float(input("Ingrese el valor en grados: "))
            x = math.radians(x)
            print(x)
            
            #Pedir el valor de terminos a sumar
            #para mayor precición
            while True:
                try:
                    n = int(input("Ingrese el numero de terminos a sumar: "))

                    senx_acum = 0.0
                    for k in range(n):
                        senx_acum = senx_acum + (-1)**k * x**(2*k+1) / math.factorial((2*k+1))

                    print("El valor del seno es: {:.10f}".format(senx_acum))
                    break 
                except ValueError:
                    print("Solo se aceptan numeros")
            break        
        except ValueError:
            print("No se aceptan caracteres distintos de Numeros")

FuncionSeno()