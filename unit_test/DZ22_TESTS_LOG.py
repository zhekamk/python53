# Завдання 1
# Створити клас Калькулятор. У класі має бути реалізовано наступну функціональність:
#  Додавання двох чисел;
#  Віднімання двох чисел;
#  множення двох чисел;
#  Розподіл двох чисел;
#  Максимум із двох чисел;
#  Мінімум із двох чисел;
#  Відсоток числа;
#  Зведення числа до ступеня.
# Протестуйте всі можливості створеного класу  за допомогою модульного тестування (unittest).
# Усі виняткові ситуації логіруйте (записуйте) до окремого файлу logs.log
# Приклад логування -
# logging.basicConfig(level=logging.WARNING, filename="logs.log", filemode='w',
#  format="We have some error: %(asctime)s : %(levelname)s : %(message)s")
# logging.error("Test str work")

import logging
logging.basicConfig(level=logging.WARNING, filename="logs.log", filemode='w',
format="We have some error: %(asctime)s : %(levelname)s : %(message)s")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return ("Помилка: Ділення на нуль неможливе")
        return a / b

    def maximum(self, a, b):
        return max(a, b)

    def minimum(self, a, b):
        return min(a, b)

    def percentage(self, number, percent):
        return (number * percent) / 100

    def power(self, base, exponent):
        return base ** exponent


c1 = Calculator()

# print(c1.add(5, 5))
# print(c1.subtract(10, 5))
# print(c1.multiply(5, 5))
# print(c1.divide(10, 0))
# print(c1.maximum(10, 5))
# print(c1.minimum(10, 5))
# print(c1.percentage(10, 20))
# print(c1.power(5, 3))

try:
    logging.warning("cant devide by zero")
    print(10 / 0)

except Exception as ex:
    logging.exception(ex)
    logging.error(ex)

try:
    print(10 + '5')

except Exception as ex:
    logging.exception(ex)
    logging.error(ex)