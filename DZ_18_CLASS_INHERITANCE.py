# Завдання 1
# Створіть клас Passport (паспорт), який міститиме паспортну інформацію про громадянина заданої країни.
# За допомогою механізму успадкування реалізуйте клас ForeignPassport (закор­дон­ний паспорт), похідний від Passport.
# Нагадаємо, що закордонний паспорт містить, крім паспортних даних, дані про візи і номер закордонного паспорта.
# Кожен із класів має містити необхідні методи




class Passport:
    def __init__(self, number_passport, date_passport, issuer, country, pib, birthday,adress):
        self._number_passport = number_passport
        self._date_passport = date_passport
        self._issuer = issuer
        self._country = country
        self._pib = pib
        self._birthday = birthday
        self._adress = adress

    @property
    def number_passport(self):
        return self._number_passport
    @number_passport.setter
    def number_passport(self, number_passport):
        self._number_passport = number_passport

    @property
    def date_passport(self):
        return self._date_passport
    @date_passport.setter
    def date_passport(self, date_passport):
        self._date_passport = date_passport

    @property
    def issuer(self):
        return self._issuer
    @issuer.setter
    def issuer(self, issuer):
        self._issuer = issuer

    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, country):
        self._country = country

    @property
    def pib(self):
        return self._pib
    @pib.setter
    def pib(self, pib):
        self._pib = pib.title()

    @property
    def birthday(self):
        return self._birthday
    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday

    @property
    def adress(self):
        return self._adress
    @adress.setter
    def adress(self, adress):
        self._adress = adress

    def getInfo(self):
        return (f"number passport: {self.number_passport},"
                f"\ndate passport: {self.date_passport},"
                f"\ncountry: {self.country},"
                f"\nissuer: {self.issuer},"
                f"\npib: {self.pib},"
                f"\nbirthday: {self.birthday},"
                f"\nadress: {self.adress}")


class Foreign_passport(Passport):
    def __init__(self, number_passport, date_passport, issuer, country, pib, birthday, adress, number_f_passport, visa):
        super().__init__(number_passport, date_passport, issuer, country, pib, birthday,adress)
        self._number_f_passport = number_f_passport
        self._visa = visa

    @property
    def number_f_passport(self):
        return self._number_f_passport
    @number_f_passport.setter
    def number_f_passport(self, number_f_passport):
        self._number_f_passport = number_f_passport


    @property
    def visa(self):
        return self._visa
    @visa.setter
    def visa(self, visa):
        self._visa = visa


    def getInfo(self):
        return (super().getInfo()+f'\nnumber foreign passport: {self._number_f_passport},'
                + f'\nvisa: {self._visa}')

p1 = Passport("КВ111111", '12.12.2000','Шевченківським РУ ГУМВС України в м. Києві', "Україна", 'Зуй Ігор Петрович', '05.06.1984', 'м.Київ, вул.Хрещатик,39,кв,6')
print(p1.getInfo())
print('*'*100)
f1=Foreign_passport("КВ111111", '12.12.2000','Шевченківським РУ ГУМВС України в м. Києві', "Україна", 'Зуй Ігор Петрович', '05.06.1984', 'м.Київ, вул.Хрещатик,39,кв,6', '', '')
f1.number_f_passport = 'FD589647'
f1.visa="EU,USA,CHINA"
print(f1.getInfo())
print('*'*100)

# Завдання 2
# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас CoffeeMachine (містить інформацію про кавомашину),
# клас Blender (містить інформацію про блендер), клас MeatGrinder (містить інформацію про м'ясорубку).
# Кожен із класів має містити необхідні для роботи методи.

class Device:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def func(self):
        return 'eлектронний пристрій, що '

    def getInfo(self):
        return f"{self.name}"+f'-це {self.func()}'


class CoffeeMachine(Device):
    def __init__(self, name, brand,color):
        super().__init__(name)
        self._brand = brand
        self._color = color

    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

    def work(self):
        return 'готує каву!'
    def getInfo(self):
        print(super().getInfo(), self.work(),
              f'brand: {self.brand}, color: {self.color}')

class Blender(Device):
    def __init__(self, name, brand,color):
        super().__init__(name)
        self._brand = brand
        self._color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def work(self):
        return 'використовується для подрібнення, змішування та збивання різних інгредієнтів!'

    def getInfo(self):
        print(super().getInfo(), self.work(),
              f'brand: {self.brand}, color: {self.color}')

class MeatGrinder(Device):
    def __init__(self, name, brand,color):
        super().__init__(name)
        self._brand = brand
        self._color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def work(self):
        return 'використовується для виготовлення мясного фаршу!'

    def getInfo(self):
        print(super().getInfo(), self.work(),
              f'brand: {self.brand}, color: {self.color}')

cof1=CoffeeMachine('Кавомашина', 'RIO', 'white')
cof1.getInfo()
bl1=Blender("Блендер", "ORION", "BLACK")
bl1.getInfo()
mg=MeatGrinder("М'ясорубка", "Grand", "grey")
mg.getInfo()
print('*'*100)



# Завдання 3
# Створіть клас Ship, який містить інформацію про кораблі. За допомогою механізму успадкування реалізуйте клас Frigate
# (містить інформацію про фрегат), клас Destroyer (містить інформацію про есмінця), клас Cruiser (містить інформацію про крейсер).
# Кожен із класів має містити необхідні для роботи методи.

class Ship():
    def __init__(self, name):
        self._name = name
        self._type = 'універсальний бойовий надводний корабель'
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, type):
        self._type = type

    def getInfo(self):
        return f"{self._name} - {self._type}"

class Frigate(Ship):
    def __init__(self, name):
        super().__init__(name)

    def displacement(self):
        self.displacement = '2.500 - 6000 tons'
        return self.displacement

    def role(self):
        self.role='пильнує підводні човни та дрібні загрози'
        return self.role

    def endurance(self):
        self.endurance = 'середня'
        return self.endurance

    def char(self):
        char_all=f',який {self.role()}, водотонажністю: {self.displacement()}, автономність: {self.endurance()}'
        return char_all

    def getInfo(self):
        return super().getInfo()+self.char()


class Destroyer(Ship):
    def __init__(self, name):
        super().__init__(name)

    def displacement(self):
        self.displacement = '6000-10000 tons'
        return self.displacement

    def role(self):
        self.role = 'захищає, і потужно атакує'
        return self.role

    def endurance(self):
        self.endurance = 'висока'
        return self.endurance

    def char(self):
        char_all = f',який {self.role()}, водотонажністю: {self.displacement()}, автономність: {self.endurance()}'
        return char_all

    def getInfo(self):
        return super().getInfo() + self.char()

class Cruiser(Ship):
    def __init__(self, name):
        super().__init__(name)

    def displacement(self):
        self.displacement = '>10000 tons'
        return self.displacement

    def role(self):
        self.role = 'керує боєм та несе величезний запас ракет'
        return self.role

    def endurance(self):
        self.endurance = 'максимальна'
        return self.endurance

    def char(self):
        char_all = f',який {self.role()}, водотонажністю: {self.displacement()}, автономність: {self.endurance()}'
        return char_all

    def getInfo(self):
        return super().getInfo() + self.char()


c1=Ship('Крейсер')
print(c1.getInfo())
f1=Frigate("Фрегат 'А113'")
print(f1.getInfo())
d1=Destroyer('Есмінець "Е258"')
print(d1.getInfo())
print(d1.role)
с1=Cruiser("Крейсер'К888'")
print(с1.getInfo())
print('*'*100)

# Завдання 4
# Запрограмуйте клас Money (об'єкт класу оперує однією валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок
# (центи, євроценти, копійки тощо).
# Реалізуйте методи виведення суми на екран, задання значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.
class Money:
    def __init__(self, dollar,cent):
        self.__dollar = dollar
        self.__cent = cent

    @property
    def dollar(self):
        return int(self.__dollar)
    @dollar.setter
    def dollar(self, dollar):
        self.__dollar = dollar


    @property
    def cent(self):
        return int(self.__cent)
    @cent.setter
    def cent(self, cent):
        self.__cent = cent

    def showPrice(self):
        return f'{self.dollar},{self.cent}'

m1=Money(1,50)
print(m1.showPrice())

class Product(Money):
    def __init__(self, dollar,cent,name):
        super().__init__(dollar,cent)
        self.__name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @staticmethod
    def price_change(d,c,change):
        d=m1.dollar*100
        #print(d)
        c=m1.cent
        #print(c)
        price=int(d+c)
        #print(price)
        new_price=price-change
        #print(new_price)
        new_price1=str(new_price)
        #print(new_price1)
        np1=new_price1[:len(new_price1)-2]
        np2=new_price1[len(new_price1)-2:]
        #print(np1)
        #print(np2)
        if len(new_price1)<=2:
            np3='0,'+np2
        else:
            np3=f'{np1},{np2}'
        print(np3)
        return np3

    def showPrice(self,change):
        price=super().showPrice()
        price_end=Product.price_change(self.dollar,self.cent,change)
        return (f'початкова ціна {self.name}:{price},'
                f'\nкінцева ціна {self.name}:{price_end},')


p1=Product(1,50,'bananas')
print(Product.price_change(1,50,10))
print(p1.showPrice(100))

print('*'*100)



# Завдання 5
# Створіть клас для конвертування температури з Цельсія у Фаренгейт, і навпаки. У класі має знаходитися два статичні методи:
#  для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розра­хувати кількість
# підрахунків температури та повернути це значення статичним методом.

class TempConvert:
    count=0
    @staticmethod
    def fareng_to_cels(f):
        TempConvert.count+=1
        return f'Температура {f} градусів по Фаренгейту = {(f-32)/1.8} градусів по Цельсію'
    @staticmethod
    def cels_to_fareng(с):
        TempConvert.count+=1
        return f'Температура {с} градусів по Цельсію = {с*1.8+32} градусів по Фаренгейту'

print(TempConvert.fareng_to_cels(50))
print(TempConvert.cels_to_fareng(50))
print(f'Кількість підрахунків температури: {TempConvert.count}')
print('*'*100)
# Завдання 6
# Створіть клас для конвертування з метричної системи в англійську, та навпаки. Реалізуйте функціональність у вигляді статичних методів.
# Обов'язково реалізуйте конвертування заходів довжини.

class LenConvert:
    count=0
    @staticmethod
    def mm_to_inch(a):
        LenConvert.count+=1
        return f'{a} mm = {a*0.0394} inch'
    @staticmethod
    def inch_to_mm(a):
        LenConvert.count+=1
        return f'{a} inch = {a*25,4} mm'

    @staticmethod
    def cm_to_inch(cm):
        LenConvert.count+=1
        return f'{cm} cm = {cm*0.3937} inch'
    @staticmethod
    def inch_to_cm(inch):
        LenConvert.count+=1
        return f'{inch} inch = {inch*2.54} cm'

    @ staticmethod
    def m_to_yard(m):
        LenConvert.count+=1
        return f'{m} m = {m*1.0936} yard'
    @staticmethod
    def yard_to_m(yard):
        LenConvert.count+=1
        return f'{yard} yard = {yard*0.9144} m'

    @ staticmethod
    def km_to_mile(km):
        LenConvert.count+=1
        return f'{km} km = {km*0.621371} mile'
    @staticmethod
    def mile_to_km(mile):
        LenConvert.count+=1
        return f'{mile} mile = {mile*1.6093} km'


print(LenConvert.mm_to_inch(50))
print(LenConvert.inch_to_mm(50))
print(LenConvert.cm_to_inch(50))
print(LenConvert.inch_to_cm(50))
print(LenConvert.m_to_yard(10))
print(LenConvert.yard_to_m(10))
print(LenConvert.km_to_mile(100))
print(LenConvert.mile_to_km(100))
print(f'Кількість підрахунків: {LenConvert.count}')