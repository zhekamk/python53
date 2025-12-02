#Рівень 1 Завдання 1
num1 = int(input("Введіть перше число:"))
num2 = int(input("Введіть друге число:"))
for num in range(num1,num2):
    if num%7==0:
        print(num,end=" ")
print()

#Рівень 1 Завдання 2
num1 = int(input("Введіть перше число:"))
num2 = int(input("Введіть друге число:"))
print("Усі числа діапазону:")
for num in range(num1, num2+1):
    print(num,end=" ")
print()
print("Усі числа діапазону в спадному порядку:")
for num in range(num2,num1-1,-1):
    print(num,end=" ")
print()
print("Усі числа,кратні 7:")
for num in range(num1, num2+1):
    if num % 7 == 0:
        print(num,end=" ")
print()
print("Кількість чисел,кратних 5:")
count = 0
for num in range(num1, num2+1):
    if num % 5 == 0:
        count += 1
print(count,end="\n")

#Рівень 2 Завдання 3
num1 = int(input("Введіть перше число:"))
num2 = int(input("Введіть друге число:"))
for num in range(num1, num2+1):
    if num % 3 == 0:
        print('"Fizz"', end=",")
print()
for num in range(num1, num2+1):
    if num % 5 == 0:
        print('"Buzz"', end=",")
print()
for num in range(num1, num2+1):
    if num % 5 == 0 and num % 3 == 0:
        print('"Fizz Buzz"', end=",")
print()
for num in range(num1, num2+1):
    if num % 5 != 0 and num % 3 != 0:
        print(num, end=",")
print()

#Рівень 2 Завдання 4
num1 = int(input("Введіть перше число:"))
num2 = int(input("Введіть друге число:"))
interval = int(input("Введіть крок(інтервал):"))
print("Усі числа діапазону із вказаним кроком:")
for num in range(num1, num2+1, interval):
    print(num,end=" ")
print()
choice=0
choice = int(input("""Виберіть порядок виведення:
    у прямому порядку - 1
    у зворотному порядку - 2\n:"""))
if choice == 1:
    for num in range(num1, num2 + 1, interval):
        print(num, end=" ")
    print()
else:
    choice == 2
    for num in range(num2, num1 - 1, - interval):
        print(num, end=" ")
    print()
print()

#Рівень 3 Завдання 5
num1 = int(input("Введіть перше число:"))
num2 = int(input("Введіть друге число:"))
if num1 > num2:
    num1,num2=num2,num1
product=1
count = False
for num in range(num1, num2+1):
    if num%4==0 and num%6!=0:
        count = True
        product*=num
if count == True:
    print("Добуток усіх чисел, що діляться на 4, "
    "але не діляться на 6:",product, end="")
else:
    count==False
    print("Таких чисел немає")
print()

#Рівень 3 Завдання 6
a = int(input("Введіть число А:"))
n = int(input("Введіть ступінь,до якого "
                 "потрібно піднести число, N:"))
result = 1
for i in range(n):
    result*=a
print("Число", a, "в степені", n, "=", result)















