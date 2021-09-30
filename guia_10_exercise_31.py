# Modular Programming

# Spanish
# Una empresa de turismo que vende viajes para egresados de colegios secundarios, 
# ofrece a tres cursos distintos la siguiente promoción: El costo del viaje por persona es de $ 1360, pero 
# si el grupo excede de las 40 personas, la empresa realiza un descuento del 5% sobre el costo total del 
# viaje para el curso. Desarrollar un programa, que cargando la cantidad de alumnos de cada uno de 
# los tres cursos, permita determinar:
# 1. El curso más numeroso
# 2. El monto del viaje para cada curso
# 3. El porcentaje que representa el monto del viaje del curso más numeroso sobre el total de la 
# ganancia de la empresa.

# English
# A tourism company that sells trips for high school graduates,
# offers the following promotion to three different courses: The cost of the trip per person is $ 1360, but
# If the group exceeds 40 people, the company makes a 5% discount on the total cost of the
# trip for the course. Develop a program that, loading the number of students from each of the
# the three courses, allow to determine:
# 1. The largest course
# 2. The amount of the trip for each course
# 3. The percentage that represents the amount of the trip of the most numerous course on the total of the
# profit of the company.



def which_major(n1, n2, n3):
    may = ''
    may_num = 0
    if n1 > n2 and n1 > n3:
        may = 'group 1'
        may_num = n1
    else:
        if n2 > n1 and n2 > n3:
            may = 'group 2'
            may_num = n2
        else:
            may = 'group 3'
            may_num = n3
    
    print('The largest course is ', may)
    return may_num

def amount(n1, n2 , n3):
    cost_1 = cost_2 = cost_3 = cost = 1360

    if n1 > 40:
        cost_1 = (cost - 68) * n1
    else: 
        cost_1 = cost * n1
    if n2 > 40:
        cost_2 = (cost - 68) * n2
    else: 
        cost_2 = cost * n2
    if n3 > 40:
        cost_3 = (cost - 68) * n3
    else: 
        cost_3 = cost * n3


    print('The cost of the group N° 1 is: $', cost_1)
    print('The cost of the group N° 2 is: $', cost_2)
    print('The cost of the group N° 3 is: $', cost_3)
    return cost_1, cost_2, cost_3


def percentage(major, n1, n2, n3):
    total = n1 + n2 + n3
    percentaje_company = (major * 100) / total
    percentaje_company = round(percentaje_company, 2)


    print('The percentaje of profit of the company with the group more amount is: ', percentaje_company,'%')

def start():  
    group1 = int(input('Input the group N°1: '))
    group2 = int(input('Input the group N°2: '))
    group3 = int(input('Input the group N°3: '))

    major = which_major(group1, group2, group3)
    amount(group1, group2, group3)
    percentage(major, group1, group2, group3)


if __name__ == '__main__':
    start()

