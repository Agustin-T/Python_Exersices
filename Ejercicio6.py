__autor__ = 'DEV-121 UTN'
# La dirección de la carrera de Ingeniería en Sistemas de la UTN Córdoba necesita un 
# programa que permita cargar el nombre de un estudiante de quinto año, el nombre del profesor 
# responsable de la Práctica Profesional Supervisada de ese estudiante, y el promedio general (con 
# decimales) del estudiante en su carrera. Una vez cargados los datos, se pide simplemente mostrarlos 
# en la consola de salida a modo de verificación, pero de forma que el nombre del practicante vaya 
# precedido de la cadena "est." y el nombre del profesor supervisor se preceda con "prof.". El promedio 
# del alumno debe mostrarse redondeado, sin decimales, en formato entero.

# entradas
print("Muestra de datos")
alumno = input("> Ingrese el nombre del estudiante: ")
profe = input("> Ingrese el nombre del profesor: ")
nota = float(input("> Ingrese la nota del estudiante(en decimales): "))

# procesos
promedio = round(nota)

# salidas
print("- El est. ", alumno," del prof. ", profe,", tiene promedio", promedio)