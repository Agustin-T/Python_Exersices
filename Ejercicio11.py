__autor__ = 'DEV-121 UTN'
#  Cargar por teclado tres números enteros y determinar y mostrar el mayor de ellos. No 
# utilice para el proceso la función max() de la librería estándar de Python: diseñe el algoritmo 
# suponiendo que tal función no existe en el lenguaje que usará para el desarrollo del programa

# entradas
print("Simulacion de funcion max()")
n1 = int(input("> Ingrese el N°1:"))
n2 = int(input("> Ingrese el N°2:"))
n3 = int(input("> Ingrese el N°3:"))

# procesos
if(n1 > n2 and n1 > n3):
    mayor = n1
elif(n2 > n3):
    mayor = n2
else:
    mayor = n3
    
# salidas
print("El N° mas grande es ",mayor)

