
fib=[ ]
print("Вивести числа Фібоначі в межах, які введені з клавіатури")
a=int(input('Vedit pochatok '))
b=int(input('Vvvedit kin '))
i=0
fib1=0
fib2=1


for i in range (25):
    fib.append(fib)

    fib1=fib2
    fib2=fib1+fib2
    
   
print(fib)


if a>b: print("Межі не коректні")
else: print("Числа (число) Фібоначі з заданої межі ") 

for f in fib:
    if f>=a and f<=b:
        print(f) 
 