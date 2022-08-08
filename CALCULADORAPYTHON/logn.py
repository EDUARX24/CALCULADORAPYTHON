
import math
import ln

def logNatural():
    
        while True:
            try: 

                ln = 0.0
                log = 0.0
                print("Calculadora")
                
                while True:
                     x = float(input("Ingrese el valor de X: "))
                     if x <= 0:
                         print("No puede ingresar negativos: ")
                     else: 
                        break

                for n in range(107):
                    ln = ln + ( 1 / (2 * n + 1)) * (( x - 1) / (x + 1)) ** (2 * n + 1)
                else:
                    ln = ln * 2
                p = 10
                for n in range(107):
                        log = log + ( 1 / (2 * n + 1)) * (( p - 1) / (p + 1)) ** (2 * n + 1)
                else:
                    log = log * 2

                resp = ln / log
                print("Logartimo del numero es: ",resp)
                
                print("Presione una tecla para continuar...")
            
                break
            except ValueError:
                print("SOLO SE ACEPTAN NUMEROS")

logNatural() 