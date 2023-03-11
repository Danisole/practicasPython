class Alumno:
    
    def __init__(self, nombre):
        self.nombre = nombre
        

    def __str__(self):
        return(f"Alumno {self.nombre}")


    def mostrarNota(self, nota):

        if 10 >= nota >= 8:

            print(f" el alumno {self.nombre} obtuvo {nota}: alumno destacado")

        elif 6 <= nota < 8:

            print(f" el alumno {self.nombre} obtuvo {nota}: alumno aprobado")

        elif nota < 6:

            print(f" el alumno {self.nombre} obtuvo {nota}: alumno desaprobado")   

        else:
            print("la norta ingresada no es valida")
