import sys
from funciones_matematicas import sumar, restar, multiplicar, dividir, potencia, py

if len(sys.argv)==3:
    primernum = int(sys.argv[1])

    sengundonum = int(sys.argv[2])

    print(f"la suma de {primernum} y {sengundonum} es igual {primernum+sengundonum}") 
    print(f"la resta de {primernum} y {sengundonum} es igual {primernum-sengundonum}") 
    print(f"la multiplicacion de {primernum} y {sengundonum} es igual {primernum*sengundonum}") 
    print(f"la division de {primernum} y {sengundonum} es igual {primernum/sengundonum:.2f}") 
    print(f"la potencia de {primernum} y {sengundonum} es igual {primernum**sengundonum}")    
    print(f" mi num de la suerte es {py}")


