# Una pequeña oficina de correos dispone de cinco casillas o boxes para guardar las 
# cartas que debe despachar. Cada casilla (que puede contener muchas cartas) está numerada con 
# números correlativos del 0 al 4. Cada carta que se recibe tiene un código postal numérico, y en base a 
# ese código el despachante debe determinar en qué box guardará la carta, pero de tal forma que el 
# mismo sistema sirva luego para saber en qué caja buscar una carta, dado su código postal. Diseñe un 
# esquema de distribución que permita cumplir este requerimiento, cargando por teclado el código 
# postal de tres cartas y mostrando en qué casilla será almacenada cada una.

# entradas
n = 5 # cantidad de boxes
print("Asignacion de cartas por codigo postal")
c1 = int(input("> Ingrese el codigo postal de la carta 1:"))
c2 = int(input("> Ingrese el codigo postal de la carta 2:"))
c3 = int(input("> Ingrese el codigo postal de la carta 3:"))

# procesos: seleccion por modulo
box1 = c1 % n
box2 = c2 % n
box3 = c3 % n

# salidas
print("- La carta ",c1," se almaceno en el box N°",box1)
print("- La carta ",c2," se almaceno en el box N°",box2)
print("- La carta ",c3," se almaceno en el box N°",box3)

__autor__ = 'DEV-121 UTN'