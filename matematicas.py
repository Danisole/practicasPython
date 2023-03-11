import sys
from funciones_matematicas import sumar, restar, multiplicar, dividir, potencia, py

# otras opciones para importar seria agregar un pseudonimo 
# import funciones_matematicas as fm
# tb 

if len(sys.argv)==3:
    primernum = int(sys.argv[1])

    sengundonum = int(sys.argv[2])

    print(f"la suma de {primernum} y {sengundonum} es igual {sumar(primernum,sengundonum)}") 
    print(f"la resta de {primernum} y {sengundonum} es igual {restar(primernum,sengundonum)}") 
    print(f"la multiplicacion de {primernum} y {sengundonum} es igual {multiplicar(primernum,sengundonum)}") 
    print(f"la division de {primernum} y {sengundonum} es igual {dividir(primernum,sengundonum):.2f}") 
    print(f"la potencia de {primernum} y {sengundonum} es igual {potencia(primernum,sengundonum)}")    
    print(f" mi num de la suerte es {py}")


