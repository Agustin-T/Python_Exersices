__autor__ = 'DEV-121 UTN'
# Cargar por teclado dos números enteros. Mostrarlos ordenados de menor a mayor.

# entradas
print("Mayor a menor")
n1 = int(input("- Ingrese un numero N°1: "))
n2 = int(input("- Ingrese un numero N°2: "))

# procesos 
if(n1 > n2):
    mayor = n1
    menor = n2
else:
    mayor = n2
    menor = n1

# salidas
print("- ",mayor,", ", menor)