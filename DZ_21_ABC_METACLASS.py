# Завдання 1. Транспорт
# Створи абстрактний клас Transport, який:
# має абстрактний метод move()
# має звичайний метод info()
# Створи класи:
# Car
# Bicycle
# Train
# Кожен клас реалізує move() по-своєму.
from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

    def info(self):
        print(f'транспортний засіб:')

class Car(Transport):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(f'автомобіль "{self.name}" рухається на 4 колесах за рахунок ДВЗ')

class Bicycle(Transport):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(f'велосипед "{self.name}" рухається на 2 колесах за рахунок педалей')

class Train(Transport):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print(f'потяг "{self.name}" рухається по коліях за рахунок електродвигуна та змінного струму')

c1=Car("Cлавута")
b1=Bicycle("Україна")
t1=Train("Сапсан")
for i in [c1,b1,t1]:
    i.info()
    i.move()
print('*'*100)

# Завдання 2 : Реалізація системи перевірки правил для класів за допомогою метакласів
# Опис завдання:
# Вам потрібно створити систему, яка забезпечує автоматичну перевірку, чи відповідають створені класи певним вимогам.
# Для цього потрібно використовувати метакласи.
# Вимоги до завдання:
# # Створіть метаклас ValidationMeta:
# Перевіряйте, чи всі методи класу починаються зі слова do_ (наприклад, do_task, do_something_else).
# Перевіряйте, чи є в класі атрибут description, і чи є він рядком.
# Створіть базовий клас ValidatedClass:
# Визначте цей клас із використанням метакласу ValidationMeta.
# Створіть кілька класів, які наслідують ValidatedClass:
# Один клас повинен відповідати всім правилам.
# Інший клас має порушувати одне з правил (наприклад, методи не починаються з do_ або відсутній атрибут description).
# Додайте виключення:
# Якщо клас порушує правила метакласу, має бути викликана помилка ValueError із поясненням, що саме не відповідає вимогам.
# Реалізуйте програму, яка створює об'єкти цих класів:
# У програмі виведіть інформацію про те, чи успішно створено кожен клас, або ж, якщо є помилка, виведіть її текст.
# Додаткові вимоги:
# Використовуйте модуль abc для визначення базового класу.
# Додайте можливість автоматичного створення відсутнього атрибуту description з дефолтним значенням, якщо його немає.

class ValidationMeta(type):
    def __new__(cls, name, bases, dict):
        for k, v in dict.items():
            if callable(v):
                if not k.startswith('do_'):
                    raise ValueError (f"Помилка в '{name}': метод '{k}' повинен починатися з 'do_'")
        # if 'do_' not in dict.keys():
        #     print("немає методу do_ в класі ", name)

        if 'description' not in dict.keys():
            print(f"У класі '{name}' відсутній 'description'")

        if not isinstance(dict.get('description'), str):
            raise ValueError(f"Клас '{name}' порушує правила: атрибут 'description' має бути рядком.")

        return type.__new__(cls, name, bases, dict)

class ValidationClass(metaclass=ValidationMeta):
    description="0"
    def do_work(self):
        pass

class CorrectVC(ValidationClass):
    description = "Цей клас відповідає вимогам"
    def do_work(self):
        pass
    print("Клас 'CorrectVC' створено успішно.")


try:
    class BadMethodName(ValidationClass):
        description = "Має метод без do_"
        def run_task(self):
            pass
except ValueError as e:
    print(f"Помилка створення 'BadMethodName': {e}")

try:
    class BadDescriptionType(ValidationClass):
        description = 12345
        def do_test(self):
            pass
except ValueError as e:
    print(f"Помилка створення 'BadDescriptionType': {e}")

