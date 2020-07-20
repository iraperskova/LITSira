number = 20
print ("Гра - вгадай число")

num = int(input("Введіть число  "))
while num != number:
    if num == number:

        break
    elif num > number:
        print("Ви ввели завелике число, спробуйте ще ")
        num = int(input("Введіть число  "))

    else:
        print("Ви ввели замале число, спробуйте ще ")
        num = int(input("Введіть число  "))

print ("Вітаємо ви перемогли '-' ")

