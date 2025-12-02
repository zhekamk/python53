#1
print('-'*20,'#1','-'*20)
try:
    namePeople=input("Введіть ім'я: ")
    agePeople=int(input('Введіть вік: '))
    if agePeople>130 or agePeople<0:
         raise ValueError("Введено некоректний вік")
    print(f"Привіт,{namePeople}! Твій вік - {agePeople}")
except ValueError as i :
    print('Помилка:',i)


#2-1
print('-'*20,'#2-1','-'*20)
namePeople=input("Введіть ім'я: ")
agePeople=int(input('Введіть вік: '))


def nameAgePeople(namePeople, agePeople):
    if agePeople>130 or agePeople<0:
        raise ValueError("Введено некоректний вік")
    print(f"Привіт,{namePeople}! Твій вік - {agePeople}")
try:
    nameAgePeople(namePeople, agePeople)
except ValueError as i:
    print('Помилка:', i)

#2-2
print('-'*20,'#2-2','-'*20)
namePeople=input("Введіть ім'я: ")
agePeople=int(input('Введіть вік: '))


def nameAgePeople(namePeople, agePeople):
    try:
        if agePeople>130 or agePeople<0:
            raise ValueError("Введено некоректний вік")
        print(f"Привіт,{namePeople}! Твій вік - {agePeople}")
    except ValueError as i:
        print('Помилка:', i)

nameAgePeople(namePeople, agePeople)

#3
print('-'*20,'#3','-'*20)
numbers1=[]
try:
    while len(numbers1)<5:
        numbers=int(input('Введіть додатні числа: '))
        numbers1.append(numbers)
    print(f'Список введених чисел: {numbers1}')
    for i in numbers1:
        if i<=0:
            raise ValueError("Введено не додатнє число!!!")
    print(f'Сума всіх чисел у списку: {sum(numbers1)}')

except ValueError as i:
       print('Помилка:', i)

#4-1
print('-'*20,'#4-1','-'*20)
numbers1=[]

while len(numbers1)<5:
    numbers=int(input('Введіть додатні числа: '))
    numbers1.append(numbers)
print(f'Список введених чисел: {numbers1}')


def sumOfnumbers (numbers1):
    for i in numbers1:
         if i<=0:
             raise ValueError("Введено не додатнє число!!!")
    print(f'Сума всіх чисел у списку: {sum(numbers1)}')


try:
    sumOfnumbers(numbers1)
except ValueError as i:
       print('Помилка:', i)

#4-2
print('-'*20,'#4-2','-'*20)
numbers2=[]

while len(numbers2)<5:
    numbers=int(input('Введіть додатні числа: '))
    numbers2.append(numbers)
print(f'Список введених чисел: {numbers2}')


def sumOfnumbers (numbers2):
    try:
        for i in numbers2:
            if i<=0:
               raise ValueError("Введено не додатнє число!!!")
        print(f'Сума всіх чисел у списку: {sum(numbers2)}')
    except ValueError as i:
        print('Помилка:', i)


sumOfnumbers(numbers2)

#5
print('-'*20,'#5','-'*20)
numbers11=[]

while len(numbers11)<5:
    numbers=int(input('Введіть числа: '))
    numbers11.append(numbers)

choice10=input('''Виберіть дію:
        1 - Відобразити список;
        2 - Отримати максимальне значення у списку;
        3 - Отримати мінімальне значення у списку;
        4 - Відобразити значення елемента за індексом;
        5 - Видалити елемент за індексом
        -:''')
#print(f'Список введених чисел: {numbers11}')
if choice10=='1':
    print(f'Список чисел: {numbers11}')
elif choice10=='2':
    print(f'Максимальне значення числа у списку: {max(numbers11)}')
elif choice10=='3':
    print(f'Мінімальне значення числа у списку: {min(numbers11)}')
elif choice10=='4':
    try:
        indexitem=int(input('Введіть індекс числа у списку: '))
        if indexitem<0 or indexitem>len(numbers11):
            raise IndexError ('Введене значення виходить за межі діапазону списку')
        print(f'Значення числа за веазаним індексом: {numbers11[indexitem]}')
    except IndexError as e:
        print('Помилка: ', e)
elif choice10=='5':
    try:
        indexitem=int(input('Введіть індекс числа у списку: '))
        if indexitem<0 or indexitem>len(numbers11):
            raise IndexError ('Введене значення виходить за межі діапазону списку')
        del numbers11[indexitem]
        print(f'Список чисел без видаленого елемента: {numbers11}')
    except IndexError as e:
        print('Помилка: ', e)

#6-1
print('-'*20,'#6-1','-'*20)


def choisVariant():
    numbers12 = []
    while len(numbers12) < 5:
        numberss = int(input('Введіть числа: '))
        numbers12.append(numberss)
    choice10=input('''Виберіть дію:
            1 - Відобразити список;
            2 - Отримати максимальне значення у списку;
            3 - Отримати мінімальне значення у списку;
            4 - Відобразити значення елемента за індексом;
            5 - Видалити елемент за індексом
            -:''')
    if choice10=='1':
        return choice1(numbers12)
    elif choice10=='2':
        return choice2(numbers12)
    elif choice10=='3':
        return choice3(numbers12)
    elif choice10=='4':
        return choice4(numbers12)
    elif choice10=='5':
        return choice5(numbers12)


def choice1 (numbers12):
    print(f'Список чисел: {numbers12}')


def choice2 (numbers12):
    print(f'Максимальне значення числа у списку: {max(numbers12)}')


def choice3 (numbers12):
    print(f'Мінімальне значення числа у списку: {min(numbers12)}')


def choice4 (numbers12):
      indexitem=int(input('Введіть індекс числа у списку: '))
      if indexitem<0 or indexitem>len(numbers12):
          raise IndexError ('Введене значення виходить за межі діапазону списку')
      print(f'Значення числа за вказаним індексом: {numbers12[indexitem]}')


def choice5 (numbers12):
        indexitem=int(input('Введіть індекс числа у списку: '))
        if indexitem<0 or indexitem>len(numbers12):
            raise IndexError ('Введене значення виходить за межі діапазону списку')
        del numbers12[indexitem]
        print(f'Список чисел без видаленого елемента: {numbers12}')


try:
    choisVariant()
except IndexError as e:
    print('Помилка: ', e)
except Exception:
    print('Введене значення повинно бути числом!!!')


choisVariant()


#6-2
print('-'*20,'#6-2','-'*20)


def choisVariant():
    numbers12 = []
    while len(numbers12) < 5:
        numberss = int(input('Введіть числа: '))
        numbers12.append(numberss)
    choice10=input('''Виберіть дію:
            1 - Відобразити список;
            2 - Отримати максимальне значення у списку;
            3 - Отримати мінімальне значення у списку;
            4 - Відобразити значення елемента за індексом;
            5 - Видалити елемент за індексом
            -:''')
    if choice10=='1':
        return choice1(numbers12)
    elif choice10=='2':
        return choice2(numbers12)
    elif choice10=='3':
        return choice3(numbers12)
    elif choice10=='4':
        return choice4(numbers12)
    elif choice10=='5':
        return choice5(numbers12)


def choice1 (numbers12):
    print(f'Список чисел: {numbers12}')


def choice2 (numbers12):
    print(f'Максимальне значення числа у списку: {max(numbers12)}')


def choice3 (numbers12):
    print(f'Мінімальне значення числа у списку: {min(numbers12)}')


def choice4 (numbers12):
    try:
        indexitem=int(input('Введіть індекс числа у списку: '))
        if indexitem<0 or indexitem>len(numbers12):
            raise IndexError ('Введене значення виходить за межі діапазону списку')
        print(f'Значення числа за вказаним індексом: {numbers12[indexitem]}')
    except IndexError as e:
        print('Помилка: ', e)


def choice5 (numbers12):
    try:
        indexitem=int(input('Введіть індекс числа у списку: '))
        if indexitem<0 or indexitem>len(numbers12):
            raise IndexError ('Введене значення виходить за межі діапазону списку')
        del numbers12[indexitem]
        print(f'Список чисел без видаленого елемента: {numbers12}')
    except IndexError as e:
        print('Помилка: ', e)


choisVariant()






