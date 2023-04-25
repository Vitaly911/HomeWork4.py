number1 = int(input('Введите количество элементов в первом массиве: '))
mass1 = []
for i in range(number1):
    mass1.append([int(j) for j in input("Веддите число для первого массива: ").split()])
min = min(mass1)
number2 = int(input('Введите количество элементов во втором массиве: '))
mass2 = []
for i in range(number2):
    mass2.append([int(j) for j in input("Веддите число для второго массива: ").split()])
print(*mass1)
print(*mass2)
i = 0
j = 0
while(i < number1):
    while(j < number2):
        if(min == mass2[j]):
            print(*min)
            j = number2
        j += 1
    mass1.remove(min(mass1))
    min = min(mass1)
    j = 0
    i += 1