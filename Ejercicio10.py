__autor__ = 'DEV-121 UTN'

# Cargar por teclado tres números enteros que se supone representan las edades de 
# tres personas. Determinar si alguno de los valores cargados era negativo, en cuyo caso informe en 
# pantalla con un mensaje tal como: Alguna es incorrecta: negativa. Si todos los valores eran positivos 
# o cero, informe que todas eran correctas

# entradas
print("Retorno de numero mayor")
n1 = int(input("> Edad N°1:"))
n2 = int(input("> Edad: N°2:"))
n3 = int(input("> Edad: N°3:"))

# procesos y salidas
if(n1 > 0 and n2 > 0 and n3 > 0):
    print("- Todos los valores son correctos")
else:
    print("- Uno de las edades ingresadas son numeros negativos")

