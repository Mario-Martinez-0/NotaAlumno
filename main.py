class Alumno:

    def resultadoAlumno(self):
        nombre = input("Ingrese el nombre del Alumno: ")
        nota = float (input("Ingrese la nota del alumno: "))
        if nota >= 3.0 and nota <= 5.0:
            print("El alumno", nombre, "ha aprobado con la nota:", nota)
        elif nota > 5.0 or nota < 0:
            print("Error en la nota ingresada", nota)
        else:
            print("El alumno", nombre, "no aprobo con la nota:", nota)

alumno = Alumno()
alumno.resultadoAlumno()