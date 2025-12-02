# number=int(input("Enter number-"))
# if number>0:
#     print("positive")
# else :
#     print("negative")
#


# age = int(input("Ведіть вік-"))
# if age>18:
#     print("Повнолітня")
# else:
#     print("Неповнолітня")

# print(2==2)
# print(2<=2)
# print(3<=2)
# print('dfs'>"sdf")

# and or
# number=5
# if number>1 and number<10:
#     print("number ok")
# else:
#     print("error number")

# year=int(input("Введіть pік-"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("year",year, "високосний")
# else:
#     print("year",year, "невисокосний")
#
# year=int(input("Введіть pік-"))
# if not year%4 and year%100 or not year%400:
#     print("year",year, "високосний")
# else:
#     print("year",year, "невисокосний")
# # 0- false 1 - true

# car_speed = 150
# if 50 <car_speed<130:     #if car_speed>50 and car_speed<130:
#     print("speed is ok")
# else:
#     print("too fast")
#
# temp=35
# if temp>=30:
#     print("very hot")
# elif temp>=20 and temp<50:
#     print("warm")
# elif temp>0 and temp<20:
#     print("cold")
# else:
#     print("very cold")

# age=18
# if age<=18:
#     print("школяр")
# elif age>18 and age<=21:
#     print("студент")
# elif age>21 and age<60:
#     print("співробітник")
# else:
#     print("помилка")
#
# total = 0
# count = 0
# lastNum = int(input("Enter upper value - "))
# for num in range(1, lastNum + 1):
#     count += 1
#     total += num
#     print("Total:", total)
#     print(count)
#     print("Avg:", total / count)

# login="admin"
# password="admin"
# if login=="admin":
#     print("your login is ok")
#     if password=="admin":
#         print("welcome in app")
#     else:
#         print("error password")
# else:
#     print("error login")
# count = ''
# for number in range(1, 101):  # Наприклад, перевіряємо числа від 1 до 100
#     if number % 5 == 0:
#         count += 1
# print("Кількість чисел, кратних 5:", count)