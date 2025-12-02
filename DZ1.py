# #1
# print("Nothing \nwill work \nunless you do")
#
# #2
# print(""""Anyone who
# \tstops
# \tlearning is old,
# \twhether at twenty or eighty"
# \tHenry Ford""")
#
# #3
# nummetr=float(input("Введіть кількість метрів-"))
# print((nummetr)*100,"сантиметрів;")
# print((nummetr)*10,"дециметрів;")
# print((nummetr)*1000,"міліметрів;")
# print((nummetr)*0.000160934,"миль;")
#
# #4
# diagonalrhomb1=float(input("Введіть довжину довшої діагоналі-"))
# diagonalrhomb2=float(input("Введіть довжину коротшої діагоналі-"))
# print("Площа ромба",diagonalrhomb1*diagonalrhomb2/2)
#
# #5
# zarplata=float(input("Зарплата за місяць-"))
# credit=float(input("Сума місячного платежу за кредитом у банку-"))
# komynalka=float(input("Заборгованість за комунальні послуги-"))
# print("Залишок",zarplata-credit-komynalka)
#
# #6
# print("Вартість поїздки на автомобілі:")
# way=float(input("Відстань у кілометрах-"))
# litr_100km=float(input("Витрата палива на 100 км-"))
# price_1litr=float(input("Ціна за літр бензину-"))
# print("Підсумок:",way*litr_100km*price_1litr/100)
# int("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))


def myGreeting1():
    print("Good morning! Have a nice day!")

def myGreeting2():
    print("Good day! Nice to see you!")

def myGreeting3():
    print("Hey! Long-time no see.")

def myGreeting4():
    print("Good night! See you tomorrow.")

myGreetingsList = (myGreeting1, myGreeting2, myGreeting3, myGreeting4)

for myGreeting in myGreetingsList:
    myGreeting()

def greetingRecipient(greetFunction):
    greetRecipient = input("name?")
    print("Dear, ", greetRecipient)

    greetFunction()
#
# for myGreetinginmyGreetingsList in myGreetingsList:
#     greetingRecipient(myGreeting)

def checkTimeOfDay():
    while True:
        timeOfDay = input("Input time of day (M-morning; D-afternoon; E- everning; N-night):")
        if timeOfDay == "M":
           return myGreetingsList[0]
        elif timeOfDay == "D":
           return myGreetingsList[1]
        elif timeOfDay == "E":
           return myGreetingsList[2]
        elif timeOfDay == "N":
           return myGreetingsList[3]
        else:
           print("Wrong input!")

for i in range(3):
    greetingRecipient(checkTimeOfDay())


