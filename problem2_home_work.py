print("Програма оцінки складності задач числами Фібоначчі")

fibs=[ ]
fib1=0
fib2=1

for i in range(25):
    fibs.append(fib1)

    fib1,fib2=fib2,fib1+fib2
    
        
while True:
    number=int(input("Введіть число "))

    if number in fibs:
         print("Задача оцінена на ",number,"балів")

         break
    else:
        print("Введіть коректне число")
       


