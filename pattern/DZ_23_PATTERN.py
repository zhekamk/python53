# 1. Реалізуйте клас для побудови автомобіля, де можна задати такі характеристики:
#
# Марка автомобіля (наприклад, "Tesla", "BMW").
# Тип кузова (наприклад, "седан", "позашляховик").
# Колір.
# Тип двигуна (наприклад, "електричний", "дизельний", "бензиновий").
# Кількість дверей.
# Наявність додаткових опцій (наприклад, "панорамний дах", "шкіряний салон", "автопілот").
#
# Завдання:
# Реалізуйте клас Car для представлення автомобіля.
# Реалізуйте клас CarBuilder, який дозволяє поетапно будувати автомобіль.
# Напишіть клас Director, який керує побудовою автомобіля.
# Продемонструйте тестування створених класів, побудувавши кілька автомобілів із різними характеристиками.


class Car:
     def __init__(self):
         self.model = None
         self.type= None
         self.color = None
         self.engine = None
         self.doors = None
         self.options = []

     def add(self, item):
         self.options.append(item)

     def __str__(self):
         return (f"Автомобіль {self.model}: {self.type}, колір {self.color}, "
                 f"двигун {self.engine}, дверей {self.doors}. Опції: {self.options}.")

class CarBuilder:
     def __init__(self):
         self.car = Car()

     def c_model(self, model):
         self.car.model = model

     def c_type(self, type):
         self.car.type = type

     def c_color(self, color):
         self.car.color = color

     def c_engine(self, engine):
         self.car.engine = engine

     def c_doors(self, doors):
         self.car.doors = doors

     def add_roof(self):
         self.car.add('панорамний дах')
     def add_saloon(self):
         self.car.add('шкіряний салон ')
     def add_autopilot(self):
         self.car.add('автопілот')

     def build(self):
         return self.car

class Director(CarBuilder):
    def c_model(self, model):
        self.car.model = model

car1 = CarBuilder()
car1.c_model('ЗАЗ')
car1.c_type('4x4')
car1.c_color('black')
car1.c_engine('водневий')
car1.c_doors(2)
car1.add_roof()
car1.add_saloon()
car1.add_autopilot()
print(car1.build())
print('*'*100)


# Завдання 2
# Створіть додаток для приготування пасти. Додаток має вміти створювати щонайменше три види пасти.
# Класи різної пасти мають містити такі методи:
# Тип пасти;
# Соус;
# Начинка;
# Добавки.
# Для реалізації використовуйте твірні патерни.
from abc import ABC,abstractmethod
class Pasta(ABC) :
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_filling(self):
        pass

    @abstractmethod
    def get_additives(self):
        pass

    def prepare(self):
        print(f"Приготування пасти: {self.get_type()}")
        print(f"- Соус: {self.get_sauce()}")
        print(f"- Начинка: {self.get_filling()}")
        print(f"- Добавки: {self.get_additives()}")


class Carbonara(Pasta):
    def get_type(self):
        return "Спагеті Карбонара"

    def get_sauce(self):
        return "Вершково-яєчний з пармезаном"

    def get_filling(self):
        return "Обсмажений бекон (гуанчале)"

    def get_additives(self):
        return "Чорний мелений перець"


class Bolognese(Pasta):
    def get_type(self):
        return "Тальятеле Болоньєзе"

    def get_sauce(self):
        return "Томатно-м'ясний соус"

    def get_filling(self):
        return "Яловичий фарш та овочеве соте"

    def get_additives(self):
        return "Тертий сир Грана Падано"


class Margarita(Pasta):
    def get_type(self):
        return "Паста Маргарита (Класика)"

    def get_sauce(self):
        return "Насичений томатний соус з оливковою олією"

    def get_filling(self):
        return "Кульки свіжої моцарели"

    def get_additives(self):
        return "Листя свіжого базиліку та морська сіль"

def pasta_factory(pasta):
    if pasta == 'Carbonara':
        return Carbonara()
    elif pasta == 'Bolognese':
        return Bolognese()
    elif pasta == 'Margarita':
        return Margarita()
    else:
        raise ValueError("Unknown pasta!")


p1=pasta_factory('Carbonara')
p1.prepare()
p2=pasta_factory('Bolognese')
p2.prepare()
p3=pasta_factory('Margarita')
p3.prepare()



# Завдання 3
# Користувач вводить з клавіатури набір чисел та шлях до файлу для збереження отриманих даних. Вам необхідно:
#
# зберегти усі отримані числа;
# знайти максимум та мінімум. Ці значення збережіть у тому ж файлі;
# вивести числа;
# вивести максимум та мінімум;
# створити клас для логування операцій. При створенні об'єкта класу зазначте, де виконується логування: на екрані або у файлі. У програмі ви можете створити лише один об'єкт класу. Усі дії програми логуйте за допомогою об'єкта цього класу.

