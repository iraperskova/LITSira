print("Вивести числа Фібоначчі в межах, які введені з клавіатури")

a=int(input("Введіть початок межі "))
b=int(input("Ведіть кінець межі "))

fib=[ ]
fib1=0
fib2=1

for i in range (50):
    fib.append(fib1)

    fib1,fib2=fib2,fib1+fib2


if a>b: print("Межі не коректні  ")
else: print(fib, "Числа (число) Фібоначчі з заданої межі ", sep='\n')

for f in fib:
    if f>=a and f<=b:
        print(f)

