print("Обчислення факторіалів чисел в діапазоні введеному з клавіатури з кроком введеним з клавіатури","/n")

import math

while True:
    a=int(input("Введіть ліву межу діапазону "))
    b=int(input("Введіть праву межу діапазону "))
    step=int(input("Введіть крок "))

    if a>=0 and b>=0 and a<=b and step>0:
        break

    else:
        print('Введіть коректні дані')

for i in range(a,b+1,step):
    print(i,"! = ", math.factorial(i))

