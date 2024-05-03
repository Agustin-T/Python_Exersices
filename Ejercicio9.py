__autor__ = 'DEV-121 UTN'
# Cargar por teclado tres números enteros. Determinar si el primero que se cargó es el 
# mayor de los tres (informe en pantalla con un mensaje tal como: Es el mayor o No es el mayor)

# entradas
print("Retorno de numero mayor")
n1 = int(input("> N°1:"))
n2 = int(input("> N°2:"))
n3 = int(input("> N°3:"))

# procesos
if(n1 > n2 and n1 > n3):
    mayor = n1
else:
    if(n2 > n3):
        mayor = n2
    else:
        mayor = n3

# salidas
print(" - El mayor ingresado es ", mayor)
