# 1)Потрібно створити клас "Фільм", в якому використовуватиметься клас-метод з ім'ям "середній_рейтинг",
# який буде обчислювати середній рейтинг всіх фільмів, створених з використанням цього класу.
# реалізуйте функцію для виведення рейтингу всіх фільмів та функцію для виведення імен.

class Film:
    rating_all=[]
    def __init__(self, name, rating):
        self.name=name
        self.rating=rating
        Film.rating_all.append(rating)

    @classmethod
    def averageRating(cls):
        return sum(cls.rating_all)/len(cls.rating_all)

    def getInfo(self):
        return f'Film name: {self.name}, rating: {self.rating}, rating all films: {self.averageRating()}'


film1=Film('Avatar',1)
print(film1.getInfo())
film2=Film('Rembo',2)
print(film2.getInfo())
film3=Film('Rembo2',3)
print(film3.getInfo())
print('*'*100)

# 2)Використовуючи механізм множинного успадкування, розробіть клас "Людина". Мають бути класи "Мозок", "Серце", "Ноги" і т.д.

class Brain:
    def __init__(self):
        self.weight='1.3 - 1.4 kg'
        self.body_mass='~2%'
    def getInfo(self):
        return f'Вага мозку: {self.weight}, відсоток від загальної маси тіла: {self.body_mass}'

class Heart:
    def __init__(self):
        self.weight='~250-300 gramm'
        self.body_mass='~0.4-0.5%'
    def getInfo(self):
        return f'Вага серця: {self.weight}, відсоток від загальної маси тіла: {self.body_mass}'

class Legs:
    def __init__(self):
        self.legs_count="2"
        self.legs_body_mass="~16-19%"

    def getInfo(self):
        return f'Кількість ніг: {self.legs_count}, відсоток від загальної маси тіла: {self.legs_body_mass}'

class Torso:
    def __init__(self):
        self.torso_comment="містить майже усі головні системи організму"
        self.torso_body_mass="~45-55%"

    def getInfo(self):
        return f'Тулуб {self.torso_comment}, відсоток від загальної маси тіла: {self.torso_body_mass}'

class Hands:
    def __init__(self):
        self.hands_count="2"
        self.hands_body_mass="~10-12%"

    def getInfo(self):
        return f'Кількість рук: {self.hands_count}, відсоток від загальної маси тіла: {self.hands_body_mass}'

class Head:
    def __init__(self):
        self.head_weight="~4.5-5.5 кг"
        self.head_body_mass="~8-12%"

    def getInfo(self):
        return f'Вага голови: {self.head_weight}, відсоток від загальної маси тіла: {self.head_body_mass}'


class Human (Brain, Heart, Legs, Torso, Hands, Head):
    def __init__(self,type):
        Brain.__init__(self)
        Heart.__init__(self)
        Legs.__init__(self)
        Torso.__init__(self)
        Hands.__init__(self)
        Head.__init__(self)
        self.type = type

    def showInfo(self):
        return (self.type + ':\n' + Brain().getInfo()
                +' \n'+Heart().getInfo()
                +' \n'+Legs().getInfo()
                +' \n'+Torso().getInfo()
                +' \n'+Hands().getInfo()
                +' \n'+Head().getInfo())

h1 = Human('Неандерталець')
print(h1.showInfo())
print('*'*100)



# 3)
# 1 Створіть базовий клас Instrument, який представлятиме загальні властивості та методи для всіх музичних інструментів.
# Визначте метод play, який має бути реалізований у підкласах.
# 2 Створіть підкласи StringInstrument, WindInstrument і PercussionInstrument, які представляють струнні, духові та ударні інструменти відповідно.
# Кожен із цих класів повинен успадковувати від Instrument та надавати свою реалізацію методу play.
# 3 Створіть додаткові підкласи для конкретних музичних інструментів, таких як Guitar, Flute та Drum.
# Ці класи повинні успадковувати від відповідних підкласів (StringInstrument, WindInstrument, або PercussionInstrument) та
# можуть додатково визначати свої унікальні методи та властивості, наприклад, метод tune для налаштування гітари.
# 4 Створіть екземпляри різних музичних інструментів та викличте метод play для кожного з них, щоб побачити,
# як кожний інструмент звучить.
# 5 Реалізуйте множинне спадкування, щоб створити новий клас HybridInstrument, який успадковує від кількох класів,
# які представляють різні види музичних інструментів. У цьому класі визначте свій метод play, що комбінує звуки від усіх успадкованих класів.
# 6 Створіть екземпляр HybridInstrument і викличте його метод play, щоб побачити, як множинне успадкування дозволяє комбінувати властивості
# та методи з кількох батьківських класів.

class Instrument:
    def __init__(self,name):
        self.name=name

    def play(self):
        print("Інструмент видає звук!")

class StringInstrument(Instrument):
    def __init__(self,name):
        super().__init__(name)

    def play(self):
        print('Cтрунні інструменти видають звук за допомогою вібрації струн!')

class WindInstrument(Instrument):
    def __init__(self,name):
        super().__init__(name)

    def play(self):
        print('Духові інструменти видають звук за допомогою вібрації повітря всередині інструмента!')

class PercussionInstrument(Instrument):
    def __init__(self,name):
        super().__init__(name)

    def play(self):
        print('Ударні інструменти видають звук за допомогою вібрації самого інструмента, в результаті механічного удару по ньому!')

class Guitar(StringInstrument):
    def __init__(self,name):
        super().__init__(name)

    def play(self):
        print('Гітара видає звук за допомогою вібрації 6 струн!')

    def tune(self):
        pass

class Flute(WindInstrument):
    def __init__(self,name):
        super().__init__(name)

    def play(self):
        print('Флейта видає звук завдяки вібрації стовпа повітря всередині інструмента!')

    def unique (self):
        print('Флейта -  єдиний духовий інструмент, де звук створюється розсіканням повітря')

class Drum(PercussionInstrument):
    def __init__(self,name):
        super().__init__(name)

    def play(self):
        print()

    def unique_drum(self):
        print('Барабани є одними з найгучніших акустичних інструментів')

class HybridInstrument(StringInstrument,WindInstrument):
    def __init__(self,name):
        super().__init__(name)

    def play(self):
        print (f'{self.name},{StringInstrument.play(self)}+{WindInstrument.play(self)}')

s1=StringInstrument('гітара')
w1=WindInstrument('арфа')
p1=PercussionInstrument('барабан')

for i in(s1,w1,p1):
    i.play()

h1=HybridInstrument('синтезатор')
h1.play()


