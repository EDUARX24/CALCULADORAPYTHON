import math 
from msvcrt import getch as STOP
from os import system as PC


class ElWAWA(): #clase para las operaciones
    def __init__(self):  #constructor 
        pass
    #inician todos los metodos
    def logNatural(self):
        
        while True:   
            
            try: 
                PC("cls")
                ln = 0.0
                print("!*****************************************!")
                print("|   FUNCIÓN PARA CALCULAR EL LOG NATURAL  |")
                print("!*****************************************!")
                while True:
                     x = float(input("Ingrese el valor de X: "))
                     if x <= 0:
                         print("No puede ingresar negativos ó Igual a 0")
                     else: 
                        break
                for n in range(850):
                    ln = ln + ( 1 / (2 * n + 1)) * (( x - 1) / (x + 1)) ** (2 * n + 1)
                else:
                    ln = ln * 2
                print("EL LOGARITMO NATURAL ES: {:.8f} ".format(ln))
                print("Presione una tecla para continuar...")
                STOP()
                break
            except ValueError:
                print("SOLO SE ACEPTAN NUMEROS")
                STOP() 
            


    # Funcion Seno
    def FuncionSeno(self):
        while True:
            PC("cls")
            try:
                print("!*****************************************!")
                print("|    FUNCIÓN PARA CALCULAR EL SENO        |")
                print("!*****************************************!")
                x = float(input("Ingrese el valor en grados: "))
                x = math.radians(x)
                print(x)
                
                #Pedir el valor de terminos a sumar
                #para mayor precición usando n
                while True:
                    try:
                        
                        n = int(input("Ingrese el numero de terminos a sumar: "))

                        senx_acum = 0.0
                        for k in range(n):
                            senx_acum = senx_acum + (-1)**k * x**(2*k+1) / math.factorial((2*k+1))

                        print("El valor del seno es: {:.10f}".format(senx_acum))
                        print("Presione una tecla para continuar...")
                        STOP()
                        break 
                    except ValueError:
                        print("Solo se aceptan numeros")
                break        
            except ValueError:
                print("No se aceptan caracteres!")
                STOP()

    def FuncionCoseno(self):
        while True:
            PC("cls")
            try:
                print("!*****************************************!")
                print("|    FUNCIÓN PARA CALCULAR EL COSENO      |")
                print("!*****************************************!")
                x = float(input("Ingrese el valor en grados: "))
                x = math.radians(x)
                print(x)
                
                #Pedir el valor de terminos a sumar
                #para mayor precición
                while True:
                    try:
                        n = int(input("Ingrese el numero de terminos a sumar: "))
                        cose_acum= 0.0
                        for k in range(n):
                            cose_acum = cose_acum + (-1)**k * x**(2*k) / math.factorial((2*k))

                        print("El valor del Coseno es: {:.10f}".format(cose_acum))
                        print("Presione una tecla para continuar...")
                        STOP()
                        break 
                    except ValueError:
                        print("Solo se aceptan numeros")
                break        
            except ValueError:
                print("No se aceptan caracteres!")
                STOP()
    

    def expo(self):
        PC("cls")
        while True:
            try:
                print("!*****************************************!")
                print("|   FUNCION PARA CALCULAR EL EXPONENCIAL  |")
                print("!*****************************************!")
                
                e = 0.0 #exponencial
                while True:#ciclo que valida solo para signos positivos
                     x = float(input("Ingrese el valor de X: "))
                     if x > 99:
                         print("!*****************************************!")
                         print("| No puede ingresar numeros mayores a 99  |")
                         print("!*****************************************!")
                     else: 
                        break

                for n in range(150):
                    e = e+x**n/math.factorial(n)
                print("Exponencial del numero es: ", e)
                print("Presione una tecla para continuar...")
                STOP()
                break
            except ValueError:
                print("SOLO SE ACEPTAN NUMEROS")

    def log(self):
        while True:
            
            try: 
                PC("cls")
                ln = 0.0
                log = 0.0
                print("!*****************************************!")
                print("|FUNCIÓN PARA CALCULAR EL LOG DE UN NUMERO|")
                print("!*****************************************!")

                while True:#ciclo que valida solo para signos positivos
                     x = float(input("Ingrese el valor de X: "))
                     if x <= 0:
                         print("No puede ingresar negativos ó Igual a 0")
                     else: 
                        break

                for n in range(107):
                    ln = ln + ( 1 / (2 * n + 1)) * (( x - 1) / (x + 1)) ** (2 * n + 1)
                else:
                    ln = ln * 2
                p = 10 # variable del ln de base 1
                for n in range(107): #ciclo para calcular el ln de 10 & dividir por ln de x
                        log = log + ( 1 / (2 * n + 1)) * (( p - 1) / (p + 1)) ** (2 * n + 1)
                else:
                    log = log * 2

                resp = ln / log
                print("El logaritmo es: {:.9f}".format(resp))
                print("Presione una tecla para continuar...")
                STOP()
                break
            except ValueError:
                print("SOLO SE ACEPTAN NUMEROS")
                STOP() 

    def tangente(self):
        tange_acum = 0.0

        while True:
                PC("cls")
                try:
                    print("!*****************************************!")
                    print("|    FUNCIÓN PARA CALCULAR LA TANGENTE    |")
                    print("!*****************************************!")
                    while True:#ciclo que valida solo para signos positivos
                     x = float(input("Ingrese el valor de X: "))
                     if x > 89:
                         print("!*****************************************!")
                         print("| No puede ingresar numeros mayores a 89  |")
                         print("!*****************************************!")
                     else: 
                        break
                    x = math.radians(x)
                    print(x)
                    
                    #Pedir el valor de terminos a sumar
                    #para mayor precición usando n
                    while True:
                        try:
                            n = int(input("Ingrese el numero de terminos a sumar: "))
                            senx_acum = 0.0
                            for k in range(n):#for para calcular seno
                                senx_acum = senx_acum + (-1)**k * x**(2*k+1) / math.factorial((2*k+1))
                                cose_acum= 0.0

                            for k in range(n): #for para calcular coseno
                                cose_acum = cose_acum + (-1)**k * x**(2*k) / math.factorial((2*k))
                            #for de operacion para tangente    
                            tange_acum =  senx_acum / cose_acum

                            print("La tangente del numero es:{:.10f}".format(tange_acum))
                            print("Presione una tecla para continuar...")
                            STOP()
                            break 
                        except ValueError:
                            print("Solo se aceptan numeros")
                    break        
                except ValueError:
                    print("No se aceptan caracteres!")
                    STOP()
                    