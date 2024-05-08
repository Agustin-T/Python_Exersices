__autor__ = 'DEV-121 UTN'
# Una compañía de alquiler de automóviles necesita un programa que calcule lo que se 
# debe cobrar a cada cliente, teniendo en cuenta el kilometraje recorrido por el cliente al devolver el 
# automóvil: 

# i. Si el cliente no superó los 300 km recorridos se deberá cobrar $500. 

# ii. Para recorridos desde más de 300 km y hasta no más de 1000 km se le cobrará $500 más el 
# kilometraje excedente a los 300, a razón de $3 por kilómetro. 

# iii. Para recorridos mayores a 1000 km se le cobrará $500 más el kilometraje excedente a los 
# 300, a razón de $1.5 por kilómetro.

# entradas
print("Calculo de Costo por km recorrido")
km = int(input("> Ingrese la cantidad de KM que el vehiculo ingreso: "))

# procesos
if(km <= 299):
    monto = 500
elif(km >= 300 and km <= 999):
    monto = 500 + ((km-300) * 3)
elif(km >= 1000):
    monto = 500 + ((km-300) * 1.5)
# salidas
print("- El monto a cobrar es de $", monto)

