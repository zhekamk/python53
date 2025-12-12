# Завдання 1
# Реалізуйте клас «Людина». Збережіть у класі: ПІБ, дату народження, контактний телефон, місто, країну, домашню адресу.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
# Додати метод is_major, який повертає True, якщо людина повнолітня (більше або одно 18 років) інакше False.
class Person:
    def __init__(self, name, birthday, tel, city, country, adress):
        self._name = name
        self.birthday = birthday
        self.tel = tel
        self.city = city
        self.country = country
        self.adress = adress

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def is_major(self):
        if 2025-self.birthday>18:
            return True
        else:
            return False

    def getInfo(self):
        return f"name: {self._name}, birthday: {self.birthday}, tel: {self.tel}, city: {self.city}, country:{self.country}, adress: {self.adress},major:{self.is_major}'"




person1 = Person("Kris", 2020 , '55-555-555', "Ukraine","Kyiv","01001"  )
print(person1.getInfo())
person1._name = "poul"
print(person1.getInfo())

# Завдання 2
# Створіть клас «Місто». Збережіть у класі: назву міста, назву регіону, назву країни, кількість жителів у місті, поштовий індекс міста,
# телефонний код міста. Реалізуйте методи класу для введення-виведення даних та інших операцій.
# Написати метод is_valid_zipcode, який повертає True якщо __zipcode містить 5 цифр.
class City:
    def __init__(self, city, region, country, population_city,zipcode,phone_code):
        self._city = city
        self._region = region
        self._country = country
        self._population_city = population_city
        self.__zipcode = zipcode
        self._phone_code = phone_code

    @property
    def city(self):
        return self._city.title()
    @city.setter
    def city(self, value):
        self._city = value

    @property
    def region(self):
        return self._region.title()
    @region.setter
    def region(self, value):
        self._region = value

    @property
    def country(self):
        return self._country.title()
    @country.setter
    def country(self, value):
        self._country = value

    @property
    def population_city(self):
        return self._population_city
    @population_city.setter
    def population_city(self, value):
        self._population_city = value

    @property
    def zipcode(self):
        return self.__zipcode
    @zipcode.setter
    def zipcode(self, value):
        self.__zipcode = value


    @property
    def phone_code(self):
        return self._phone_code
    @phone_code.setter
    def phone_code(self, value):
        self._phone_code = value

    def is_valid_zipcode(self):
        if len(self.__zipcode) == 5:
            return True
        else:
            return False

    def getInfo(self):
        return  (f"city: {self._city},"
                f"region: {self._region}",
                f"country: {self._country}",
                f"population of city: {self._population_city}",
                f"post index:{self.__zipcode},{self.is_valid_zipcode()} ",
                f"phone index: {self._phone_code}")

city1 = City("Kyiv", 'central','Ukraine', '40000000', '00101', '044')
print(city1.getInfo())
city1.population_city=60000000
print(city1.getInfo())


# Завдання 3
# Створіть клас «Країна». Збережіть у класі: назву країни, назву континенту, кількість жителів країни, телефонний код країни, назву столиці,
# назву міст країни. Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Country:
    def __init__(self, country,continent,population_country,phone_code,city_names):
        self._country = country
        self._continent = continent
        self._population_country = population_country
        self._phone_code = phone_code
        self._city_names = city_names

    @property
    def country(self):
        return self._country.title()
    @country.setter
    def country(self, value):
        self._country = value

    @property
    def continent(self):
        return self._continent.title()
    @continent.setter
    def continent(self, value):
        self._continent = value

    @property
    def population_country(self):
        return self._population_country

    @population_country.setter
    def population_country(self, value):
        if value <=0:
            raise ValueError("population_country must be greater than 0")
        self._population_country = value

    @property
    def phone_code(self):
        return self._phone_code
    @phone_code.setter
    def phone_code(self, value):
        self._phone_code = value

    @property
    def city_names(self):
        return self._city_names.title()
    @city_names.setter
    def city_names(self, value):
        self._city_names = value

    def getInfo(self):
        return (f"country: {self._country},"
                f"continent: {self._continent},"
                f"population country: {self._population_country},"
                f"phone code: {self._phone_code},"
                f"city names: {self._city_names}")

c1=Country("India", "Asia", 120000000, "555", "Deli, Bombei")
print(c1.getInfo())
c1.population_country=20000000
print(c1.getInfo())

# Завдання 4
# Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

# Завдання 5
# Реалізуйте клас «Книга». Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
