'''
Cargar por teclado dos números enteros. Mostrarlos ordenados de menor a mayor.
'''


print('/' * 79)
print('Calculo de menor/mayor:')
print('-' * 79)
print('Ingrese 2 numeros enteros para calcular el mayor/menor: ')

a = int(input('N°1: '))
b = int(input('N°2: '))

if a > b:
    print('Mayor: ', a)
    print('Menor: ', b)
else:
    print('Mayor: ', b)
    print('Menor: ', a)
