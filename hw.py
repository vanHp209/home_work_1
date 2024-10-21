import random

name = input("Введіть своє ім'я: ")
age = int(input("Введіть свій вік: "))
print(f"Привіт {name}, тобі {age}!")

age = int(input("Введіть свій вік: "))
if age >= 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

number = random.randint(1, 10)
attempts = 3

for i in range(attempts):
    guess = int(input("Вгадай число від 1 до 10: "))
    if guess > number:
        print("Менше")
    elif guess < number:
        print("Більше")
    else:
        print("Ви вгадали!")
        break
else:
    print(f"Ви програли! Загадане число було: {number}")

    x = int(input("Введіть перше число: "))
    y = int(input("Введіть друге число: "))

    if x > y:
        x, y = y, x

    for i in range(x, y + 1):
        print(i, end=' ')

n = int(input("Введіть число: "))

for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i, end=' ')

factorial_number = int(input("Введіть число: "))

def factorial(number):
    if number < 2:
        return 1
    else:
        return number * factorial(n-1)

print(f"Факторіал {n} = {factorial(factorial_number)}")
