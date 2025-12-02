# ЦИКЛИ FOR WHILE
from random import choice

# for i in collection:
# дія

# for i in 1, 2, 3, 4, 5:
#     print(i)
#
# for s in "python":
#     print(s, end=" ")
#
# print("\nend for")
#
# # range() - генерує діапазон чисел від 0 до числа яке вказано як аргумент
#
# for num in range(5):
#     print(num)
#
# print("----------------")
# for num in range(1, 11):
#     print(num)
#
# print("----------------")
# for num in range(1, 11, 2):
#     print(num)

print("----------------")
for num in range(10, 0, -1):
    print(num)

# if 'n' in "small":
#     print("yes")
# else:
#     print("no")
#
# total = 0
# count = 0
# lastNum = int(input("Enter upper value - "))
# for num in range(1, lastNum + 1):
#     count += 1
#     total += num
#
# print("Total:", total)
# print(count)
# print("Avg:", total / count)

# while умова:
# тіло цикла

# count = 0
# while count < 10:
#     count += 1
#     print("count:", count)
#
# from random import randint
#
# randNum = randint(1, 100)
# userNum = 0
# print(randNum)
# while userNum != randNum:
#     userNum = int(input("Enter num 1-100 - "))
#     if userNum < randNum:
#         print("Try higher...")
#     elif userNum > randNum:
#         print("Try lower...")
# else:
#     print("Winnner!")
#
# password = "admin"
# user_pass = ""
#
# while user_pass != password:
#     user_pass = input("enter password - ")
# else:
#     print("Success")

# break / continue
# num = 0
# while True:
#     num = int(input("Enter num - "))
#     if num == 0:
#         print("Stop")
#         break
#
#     if num % 2 == 0:
#         print(num)
#     else:
#         print("next iteration")
#         continue
# #
# for num in range(20):
#     if num == 10:
#         break
#     print(num)

# вкладені конструкцї

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print()

#1
num1 = int(input("Введіть перше число:"))
num2 = int(input("Введіть друге число:"))
for num in range(num1,num2):
    print(num,end=" ")
print()
#2
num1 = int(input("Введіть перше число:"))
num2 = int(input("Введіть друге число:"))
for num in range(num1,num2):
    if num % 2 != 0:
        print(num,end=" ")
print()

#3
line=0
line = int(input("Введіть довжину лінії:"))
for num in range(1,line+1):
    print("*",end="")
print()

#4
height_rectangle = int(input("Введіть висоту прямокутника:"))
width_rectangle = int(input("Введіть ширину прямокутника:"))
for i in range(height_rectangle):
    for y in range(width_rectangle):
        print("*",end="")
    print()

#5
choice=0
while choice <5E100:
    choice = int(input("""Потрібно:
    1) додати два числа?
    2) відняти два числа?
    3) подiлити два числа?
    4) вихід?
    Виберіть варіант:"""))
    if choice == 1:
        num1 = float(input("Введіть перше число:"))
        num2 = float(input("Введіть друге число:"))
        print(num1, "+", num2, "=", num1+num2)
        break
    elif choice == 2:
        num1 = float(input("Введіть перше число:"))
        num2 = float(input("Введіть друге число:"))
        print(num1, "-", num2, "=", num1-num2)
        break
    elif choice == 3:
        num1 = float(input("Введіть перше число:"))
        num2 = float(input("Введіть друге число:"))
        print(num1, "/", num2, "=", num1/num2)
        break
    elif choice == 4:
        print("Exit")
        break
    else:
        choice > 4
        print("Введено некоректне число!!!")
        continue



#     if num == 0:
#         print("Stop")
#         break
#
#     if num % 2 == 0:
#         print(num)
#     else:
#         print("next iteration")
#         continue













