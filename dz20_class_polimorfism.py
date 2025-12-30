import json
# Завдання 1
# Створіть клас Airplane (Літак). За допомогою перевантаження операторів, реалі­зуйте:
# перевірку на рівність типів літаків (операція = =);
# збільшення та зменшення пасажирів у салоні літака (операції +, -, +=, -=);
# порівняння двох літаків за максимально можливою кількістю пасажирів на борту (операції >, <, <=, >=).

class Airplane:
    def __init__(self, type,passengers):
        self.type = type
        self.passengers = passengers

    def getInfo(self):
        return f'Тип літака: {self.type}, кількість пасажирів: {self.passengers}'

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.type == other.type and self.passengers == other.passengers

    def __add__(self, other):
        add=other.passengers if isinstance(other, Airplane) else other
        return f'{self.type}, {self.passengers+add}'

    def __sub__(self, other):
        sub=other.passengers if isinstance(other, Airplane) else other
        if self.passengers>sub:
            return f'{self.type}, {self.passengers-sub}'

    def __iadd__(self, other):
        add=other.passengers if isinstance(other, Airplane) else other
        return f'{self.type}, {self.passengers+add}'

    def __isub__(self, other):
        sub=other.passengers if isinstance(other, Airplane) else other
        return f'{self.type}, {self.passengers-sub}'

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers<other.passengers

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.passengers<=other.passengers

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers>other.passengers

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.passengers>other.passengers


a1=Airplane('AН-124', 100)
print(a1.getInfo())
a2=Airplane('AН-225', 200)
print(a2.getInfo())
a3=Airplane('AН-225', 200)
print(a3.getInfo())
print(a1==a2)
print(a2==a3)
a4=a1+a2
print(a4)
a5=a1+20
print(a5)
a6=a2-a1
print(a6)
a7=a3-50
print(a7)
a1+=10
print(a1)
a2-=15
print(a2)
print(a1<a2)
print(a1>a2)
print(a1>=a2)
print(a1<=a2)
print('*'*100)

# Завдання 2
# Створіть клас Flat (Квартира). Реалізуйте перевантажені оператори:
# перевірку на рівність площ квартир (операція ==);
# перевірку на нерівність площ квартир (операція !=);
# порівняння двох квартир за ціною (операції >, <, <=, >=).

class Flat:
    def __init__(self, number_flat, square, price):
        self.number_flat = number_flat
        self.square = square
        self.price = price

    def getInfo(self):
        return f'Номер квартири: {self.number_flat}, площа: {self.square}, ціна: {self.price}'

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.square==other.square

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.square!=other.square

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price<other.price

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price<=other.price

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price>other.price

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price>=other.price

f1=Flat('10',58,100000 )
f2=Flat('50',120,300000 )
f3=Flat('20',58,110000 )
for f in [f1,f2,f3]:
    print(f.getInfo())
print(f1==f2)
print(f1==f3)
print(f1>f2)
print(f1<f3)
print(f1>=f3)
print(f1<=f2)
print('*'*100)


# Завдання 3
# Створіть базовий клас Shape для рисування плоских фігур. Визначте методи:
# Show() — виведення на екран інформації про фігуру;
# Save() — збереження фігури у файл;
# Load() — зчитування фігури з файлу.
# Визначте похідні класи:
# Square — квадрат із заданими з координатами лівого верхнього кута та дов­жи­ною сторони.
# Rectangle — прямокутник із заданими координатами верхнього лівого кута та розмірами.
# Circle — коло із заданими координатами центру та радіусом.
# Ellipse — еліпс із заданими координатами верхнього кута описаного навколо нього прямокутника зі сторонами, паралельними осям координат, та розмірами цього прямокутника.
# Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну фігуру.

class Shape:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def showInfo(self):
        return f'x: {self.x}, y: {self.y}'

    def saveInfo(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(self.__dict__, file, indent=4)
        except Exception as e:
            print(e)

    def loadInfo(self,filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data

class Square(Shape):
    def __init__(self, x,y,side):
        super().__init__(x,y)
        self.side = side

    def showInfo(self):
        return f'квадрат із заданими з координатами лівого верхнього кута: {super().showInfo()} та довжиною сторони: {self.side}'

class Rectangle(Shape):
    def __init__(self, x,y,width,height):
        super().__init__(x,y)
        self.width = width
        self.height = height

    def showInfo(self):
        return f'прямокутник із заданими координатами верхнього лівого кута: {super().showInfo()} шириною: {self.width} та висотою: {self.height}'

class Circle(Shape):
    def __init__(self, x,y,radius):
        super().__init__(x,y)
        self.radius = radius

    def showInfo(self):
        return f'коло із заданими координатами центру: {super().showInfo()} та радіусом: {self.radius}'


class Ellipse(Shape):
    def __init__(self, x,y,width,height):
        super().__init__(x,y)
        self.width = width
        self.height = height

    def showInfo(self):
        return (f'еліпс із заданими координатами верхнього кута описаного навколо нього прямокутника зі сторонами, '
                f'паралельними осям координат: {super().showInfo()} та розмірами цього прямокутника: '
                f'шириною: {self.width} та висотою: {self.height}')



s1=Square(10,20,5)
print(s1.showInfo())
s1.saveInfo('square.json')
print(s1.loadInfo('square.json'))
r1=Rectangle(10,20,5,10)
r1.saveInfo('rectangle.json')
c1=Circle(10,20,5)
c1.saveInfo('circle.json')
e1=Ellipse(10,20,5,10)
e1.saveInfo('ellipse.json')

s1_new=Square.loadInfo('square.json')
r1_new=Rectangle.loadInfo('rectangle.json')
c1_new=Circle.loadInfo('circle.json')
e1_new=Ellipse.loadInfo('ellipse.json')

for f in [s1_new,r1_new,c1_new,e1_new]:
   print(f.showInfo())







