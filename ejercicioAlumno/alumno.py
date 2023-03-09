import sys

class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return(f"Alumno {self.nombre} {self.nota}")


    if len(sys.argv)==3:

        nombre = sys.argv[1]

        nota = int(sys.argv[2])

        # print(f"el alumno {nombre} obtuvo en su examen de python {nota}")

        def mostrarNota(self, nombre, nota):

            if 10 >= nota >= 8:

                print(f" el alumno {nombre} obtuvo {nota}: alumno destacado")

            elif 6 <= nota < 8:

                print(f" el alumno {nombre} obtuvo {nota}: alumno aprobado")

            elif nota < 6:

                print(f" el alumno {nombre} obtuvo {nota}: alumno desaprobado")   

            else:
                    print("la norta ingresada no es valida")
    else:
        print("no ingresaste la cantidad correcta de parametros")