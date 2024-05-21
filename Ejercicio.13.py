__autor__ = 'DEV-121 UTN'

# Se cargan por teclado las notas obtenidas por un estudiante en tres parciales 
# realizados durante el cursado de una materia universitaria. Además, se carga la nota final que ese 
# estudiante obtuvo en el desarrollo de los trabajos prácticos en esa misma materia. Se sabe que al 
# terminar el cursado de la materia, todo alumno puede quedar en uno de los siguientes estados 
# académicos:
# a. Libre: si no llegó a cumplir con las condiciones para ser Regular.
# b. Regular: si aprobó al menos dos de los tres parciales con nota de 4 o más y además obtuvo 
# nota de 4 o más en la nota final de trabajos prácticos.
# c. Promocionado: si aprobó los tres parciales con nota de 7 o más pero con promedio entre ellos 
# de 8(ocho) o más, y además obtuvo nota de 8 o más en la nota final del práctico.
# d. Aprobado: si aprobó los tres parciales con nota de 7 o más pero con promedio entre ellos de 
# 9(nueve) o más, y además obtuvo nota de 8 o más en la nota final del práctico.
# El programa debe determinar y mostrar por pantalla el estado en que finalmente quedó el estudiante.

nota1 = int(input("> Ingrese las nota del parcial 1: "))
nota2 = int(input("> Ingrese las nota del parcial 2: "))
nota3 = int(input("> Ingrese las nota del parcial 3: "))
notatp = int(input("> Ingrese las nota final del TP: "))

Libre = True
Regular = False
Promocionado = False
Aprobado = False
status = 0


if(nota1 >= 4):
    status += 0.5
if(nota2 >= 4):
    status += 0.5
if(nota3 >= 4):
    status += 0.5
if(status >= 1 & notatp >= 4):
    Libre = False
    Regular = True
if(nota1 >= 7 & nota2 >= 7 & nota3 >= 7 & ((nota1 + nota2 + nota3) % 3 >= 8) & notatp >= 8):
    Regular = False
    Promocionado = True
if(nota1 >= 7 & nota2 >= 7 & nota3 >= 7 & ((nota1 + nota2 + nota3) % 3 >= 9) & notatp >= 8):
    Promocionado = False
    Aprobado = True

resultado = ""
if(libre == True){
    resultado = 'Libre'
}
if(Regular == True){
    resultado = "Regular"
}
if(Promocionado == True){
    resultado = "Promocionado"
}
if(Aprobado == True){
    resultado = "Aprobado"
}

print("- El estado final del alumno en la materia es: ", resultado)