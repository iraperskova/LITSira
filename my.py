number=20
print("Гра - вгадай число")

nume=int(input("Введіть число  "))
while nume!=number:
    if nume == number:

        break
    elif nume > number:
        print("Ви ввели завелике число, спробуйте ще ")
        nume=int(input("Введіть число  "))

    else:
        print("Ви ввели замале число, спробуйте ще ")
        nume=int(input("Введіть число  "))

print("Вітаємо ви перемогли  ")