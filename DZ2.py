#Рівень1 Завдання1

num1 = int(input("Введіть перше число:"))
num2 = int(input("Введіть друге число:"))
num3 = int(input("Введіть третє число:"))
select = input("Додати все? +, чи перемножити все? *")
if select== '+':
    print(num1,"+",num2, "+", num3, "=", num1+num2+num3)
else:
    print(num1, "*", num2, "*", num3, "=", num1*num2*num3)

#Рівень1 Завдання2

num1 = int(input("Введіть перше число:"))
num2 = int(input("Введіть друге число:"))
num3 = int(input("Введіть третє число:"))
select = input("Потрібно вибрати:\nМаксмальне число, max;\nМінімальне число, min; \nСередньоарифметичне трьох чисел,average:")
if select== 'max':
    print("Максимальне число",max(num1,num2,num3))
elif select== 'min':
    print("Мінімальне число",min(num1,num2,num3))
elif select== 'average':
    average = (num1 + num2 + num3) / 3
    print("Середньоарифметичне трьох чисел",average)

#Рівень2 Завдання3

mark = int(input("Поставте оцінку від 1 до 5:"))
if mark==1:
    print("Дуже погано.")
elif mark == 2:
    print("Погано.")
elif mark == 3:
    print("Задовільно.")
elif mark == 4:
    print("Добре.")
elif mark == 5:
    print("Відмінно.")
else:
    print("Вказана невірна оцінка.")

#Рівень2 Завдання4

metr=float(input("Введіть кількість метрів:"))
select = input("""Перевести:
\t 1. В милі, дюйми або ярди?
\t 2. Одразу в милі, дюйми та ярди?
\t 3. В кілометри та сантиметри?
\t\t Виберіть варіант:""")

if select== '1':
    select1 = input("""Перевести:
    1. В милі?
    2. В дюйми?
    3. В ярди?
    \t Виберіть варіант:""")
    if select1 == '1':
        print(metr, "метр = ", metr*0.000621371, "миль")
    elif select1 == '2':
        print(metr, "метр = ", metr*39.3701, "дюйм")
    elif select1 == '3':
        print(metr, "метр = ", metr*1.09361, "ярд")

elif select== '2':
    print(metr, "метр = ", metr * 0.000621371, "миль")
    print(metr, "метр = ", metr * 39.3701, "дюйм")
    print(metr, "метр = ", metr * 1.09361, "ярд")

elif select== '3':
    print(metr, "метр = ", metr * 0.001, "кілометр")
    print(metr, "метр = ", metr * 100, "сантиметр")

#Рівень3 Завдання5

num1 = float(input("Введіть перше число:"))
num2 = float(input("Введіть друге число:"))
select = input("""Потрібно:
1) додати?
2) відняти?
3) помножити?
4) поділити?
5) знайти залишок?
6) піднести до степеня?
Виберіть варіант:""")
if select== '1':
    print(num1,"+",num2,"=",num1+num2)
elif select== '2':
    print(num1,"-",num2,"=",num1-num2)
elif select == '3':
    print(num1, "*", num2, "=", num1*num2)
elif select== '4':
    print(num1,"/",num2,"=",num1/num2)
elif select== '5':
    print(num1,"залишок від ділення на",num2,"=",num1%num2)
elif select== '6':
    print(num1,"в степені",num2,"=",num1**num2)

#Рівень3 Завдання6

num3 = int(input("Введіть тризначне число:"))
zyfra1=num3//100
zyfra2=num3//10%10
zyfra3=num3%10
if zyfra1==zyfra2==zyfra3:
    print("Всі цифри однакові")
else:
    print("Цифри різні")









