import pickle
import string
import os
import json


#1
print('-'*20,'#1','-'*20)

def serialize(file_name, data):
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)


def deserialize(file_name):
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
    return data

def main():
    try:
        numbers = input('Введіть цілі числа: ')
        numbers = numbers.split()
        numbers1 = list(map(int, numbers))
        print(f'список до серіалізації: {numbers1}')
        file_name = "numbers.data"
        serialize(file_name, numbers1)
        numbers_deser = deserialize(file_name)
        print(f"список після серіалізації: {numbers_deser}")
    except ValueError:
        print('Помилка! Введено не вірні дані! Введіть цілі числа, використовуючи пробіл!')
    except Exception as ex:
        print(ex)


main()

#2
print('-'*20,'#2','-'*20)
import json

def json_serialize(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)
        print('Дані збережено!')


def json_deserialize(file_name):
    with open(file_name, 'r') as file:
        data=json.load(file)
        print(f'Дані завантажено - список цілих чисел: {data}')
    return data


def addNumber(file_name, data):
    try:
        #json_deserialize(file_name)
        numbers = input('Введіть цілі числа, використовуючи пробіл: ')
        numbers = numbers.split()
        numbers3 = list(map(int, numbers))
        numbers4 = data+numbers3
        print(f'Нові дані:{numbers4}')
        json_serialize(file_name, numbers4)
    except ValueError:
        print('Помилка! Введено не вірні дані! Введіть цілі числа, використовуючи пробіл!')
    except Exception as ex:
        print(ex)


def delNumber(file_name):
    try:
        data=json_deserialize(file_name)
        numbers = input('Введіть ціле число(ла), використовуючи пробіл: ')
        numbers = numbers.split()
        numbers5 = list(map(int, numbers))
        for i in numbers5:
            if i in data:
                data.remove(i)
            else:
                 print(f'числа {i} не знайдено! ')
        print(f'Нові дані:{data}')
        json_serialize(file_name, data)
    except ValueError:
        print('Помилка! Введено не вірні дані! Введіть цілі числа, використовуючи пробіл!')
    except Exception as ex:
        print(ex)


def menu():
    try:
        file_name='numbersList.txt'
        numbers2 = [1,2,3,4,5,6,7,8,9]
        json_serialize(file_name, numbers2)
        while True:
            print("1. Завантажити дані ")
            print("2. Зберегти дані")
            print("3. Додати дані")
            print("4. Видалити дані")
            print("5. Exit ")
            choice = input("Enter num - ")
            if choice == '1':
                json_deserialize(file_name)
            elif choice == '2':
                 json_serialize(file_name, numbers2)
            elif choice == '3':
                 num=json_deserialize(file_name)
                 addNumber(file_name,num)
            elif choice == '4':
                 delNumber(file_name)
            elif choice == '5':
                break
            else:
                print("Error menu choice !")
    except Exception as ex:
        print(ex)


menu()

#3
print('-'*20,'#3','-'*20)



user_file='userlist.txt'
user_passwords = {
    'admin': 'SecurePassword123!',
    'ivan_ko': 'Ivanko_2024',
    'olena_s': 'OlenkaBestPass',
    'guest': 'password123',
    'max_z': 'StrongPass#456'
}


def first_data():
    print('Початковий список:')
    with open(user_file, 'w') as file:
        json.dump(user_passwords, file, indent=4)
    with open(user_file, 'r') as file:
        user=json.load(file)
        for key, val in user.items():
            print(f"{key}: {val}")



def add_user(login, password):
    try:
        with open(user_file, 'r') as file:
             user=json.load(file)
             user.update({login: password})
        with open(user_file, 'w') as file:
             json.dump(user, file, indent=4)
        print("Реєстрація пройшла успішно!")
    except Exception as ex:
        print("Помилка введення даних !", ex)

def del_user(login, password):
    try:
        with open(user_file, 'r') as file:
            user = json.load(file)
            new_user={}
            for key, value in user.items():
                if key!=login and value!=password:
                    new_user.update({key:value})
            else:
                del user[login]
        with open(user_file, 'w') as file:
            json.dump(new_user, file, indent=4)
            print(f'Дані користувача: {login} - видалено!')
    except Exception as ex:
        print("Помилка введення даних !", ex)


def find_user(login):
    try:
        with open(user_file, 'r') as file:
            user = json.load(file)
            for key in user.keys():
                if key == login:
                    print(f'Користувача: {login} знайдено! Пароль: {user[login]}')
                    break
            else:
                print(f'Користувача: {login} не знайдено!')
    except Exception as ex:
        print("Помилка введення даних !", ex)


def change_user():
    try:
        keyName = input("Введіть логін: ")
        keyValue = input("Введіть пароль: ")
        with open(user_file, 'r') as file:
            user = json.load(file)
            find_user(keyName)
            for key, value in user.items():
                if key == keyName and value == keyValue:
                   keyValue1=input(f'введіть новий пароль:')
                   user.update({keyName: keyValue1})
                   print("Пароль змінено!")
        with open(user_file, 'w') as file:
            json.dump(user, file, indent=4)
    except Exception as ex:
        print("Помилка введення даних !", ex)


def view_userList():
    try:
        with open(user_file, 'r') as file:
            user = json.load(file)
            print('Cписок користувачів:')
            for key, val in user.items():
                print(f"{key}: {val}")
    except Exception as ex:
        print(ex)

def mainDict():
    try:
        while True:
            print("1. Додати дані ")
            print("2. Видалити дані")
            print("3. Пошук даних")
            print("4. Редагування даних")
            print("5. Збереження даних")
            print("6. Завантаження даних")
            print("7. Вихід ")
            choice = input("Зробіть вибір - ")
            if choice == '1':
                print('Реєстрація нового користувача!')
                login=input('Введіть логін: ')
                password=input('Введіть пароль: ')
                add_user(login,password)
            elif choice == '2':
                print('Видалення користувача!')
                login = input('Введіть логін: ')
                password = input('Введіть пароль: ')
                del_user(login, password)
            elif choice == '3':
                print('Пошук користувача!')
                login = input('Введіть логін: ')
                find_user(login)
            elif choice == '4':
                 change_user()
            elif choice == '5':
                 print('Дані збережено!!!')
            elif choice == '6':
                 view_userList()
            elif choice == '7':
                 print('Завершення програми!')
                 break
            else:
                print("Помилка вибору! Спробуйте ще!")
    except Exception as ex:
        print(ex)

first_data() # коментується після першого виклику
mainDict()