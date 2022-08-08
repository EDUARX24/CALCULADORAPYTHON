
import math

from sympy import factor
import ln
def expo():

    x = int(input("Ingrese x: "))
    e = 0.0

    for n in range(50):
        e = e+x**n/math.factorial(n)
    print("X es: ", e)


expo()