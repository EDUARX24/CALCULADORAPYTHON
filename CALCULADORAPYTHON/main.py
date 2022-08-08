#Calculadora final
from functools import cache
from ln import ElWAWA
from os import system as PC
import pyfiglet

txt = pyfiglet.figlet_format("Hasta pronto :D")
ms =  pyfiglet.figlet_format("CALCULADORA")

def menu():
    calcular = ElWAWA()
    menu = "nada"
    
    while menu != "7":
        PC("cls")
        print(ms)
        print("|****************************************|")
        print("|        CALCULADORA 2M1-C0              |")
        print("|----------------------------------------|")
        print("|   **POR FAVOR SELECCIONE UNA OPCIÓN**  |")
        print("|----------------------------------------|")
        print("| 1. CALCULAR EL SENO                    |")
        print("|----------------------------------------|")
        print("| 2. CALCULAR EL COSENO                  |")
        print("|----------------------------------------|")
        print("| 3. CALCULAR EXPONENCIAL                |")
        print("|----------------------------------------|")
        print("| 4. CALCULAR LOG NATURAL                |")
        print("|----------------------------------------|")
        print("| 5. CALCULAR LOGARTIMOS                 |")
        print("|----------------------------------------|")
        print("| 6. CALCULAR TANGENTE                   |")
        print("|----------------------------------------|")
        print("| 7. SALIR      ===>                EXIT |")
        print("|****************************************|")

        menu = input("INGRESE UNA OPCION: ")

        if menu == "1":
            calcular.FuncionSeno() 
           
        elif menu == "2":
           calcular.FuncionCoseno()

        elif menu == "3":
            calcular.expo()

        elif menu == "4":
            calcular.logNatural()

        elif menu == "5":
            calcular.log()
        
        elif menu == "6":
            calcular.tangente()

    
    return menu

                 
# Funcion prnicipal
if __name__ == "__main__": 

    while True:
        try:
            menu()
            PC("cls")
            print(txt)
            break
        except (EOFError, KeyboardInterrupt):
            print("ERRROR")