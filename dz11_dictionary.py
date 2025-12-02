#1
print('-'*20,'#1','-'*20)
capitals = {"Україна": "Київ", "Польща": "Варшава", "Німеччина": "Берлін"}
for key in capitals:
    print(f'Name country: {key}')
for key, value in capitals.items():
    print(f'Capital of country {key}: {value}')
capitals.update([('Франція','Париж')])
for key in capitals:
    print(key,'-', capitals[key])

#2
print('-'*20,'#2','-'*20)
prices={"яблуко": 15, "банан": 20, "груша": 18}
keyfruits=input('Введіть назву товару: ')
if keyfruits in prices:
   print(f'Ціна {keyfruits} = {prices[keyfruits]}, грн')
else:
    print('Такого товару немає в магазині')


#3
print('-'*20,'#3','-'*20)


def inputInfo():
    locks=['ПІБ', 'телефон', 'корпоративний email', 'назва посади',
                       'номер кабінету', 'Skype']
    firmsInfoPeople = []
    while True:
        firmsInfoPeople1={}
        for i in locks:
            j= input(f'Введiть {i} співробітника:')
            firmsInfoPeople1[i]=j
        firmsInfoPeople.append(firmsInfoPeople1)
        answer = input('Ввести інфо про ще одного співробітника? так/ні: ')
        if answer != 'так':
            break

    return firmsInfoPeople


firmsInfoPeople=inputInfo()
print(firmsInfoPeople)
print(len(firmsInfoPeople))

def findInfo(firmsInfoPeople):
    keyName = input("Введіть тип пошуку: ")
    keyValue = input("Введіть значення пошуку: ")

    for item in firmsInfoPeople:
        if item.get(keyName) == keyValue:
            print("Співробітник знайдений !")
            for key, val in item.items():
                print(f"{key}: {val}")
            return item
    return print("Співробітник не знайдений")


findInfo(firmsInfoPeople)


def changeInfo(firmsInfoPeople):
    keyName = input("Введіть тип даних, що потрібно змінити: ")
    keyValue = input("Введіть значення пошуку: ")

    for item in firmsInfoPeople:
        if item.get(keyName) == keyValue:
           keyValue1=input(f'введіть нове значення {keyName}')
           item.update({keyName: keyValue1})
           print("ІНФО ЗМІНЕНО!")
           for key, val in item.items():
                print(f"{key}: {val}")
           return item
    return print("ДАНІ НЕ ЗМІНЕНО")


changeInfo(firmsInfoPeople)


def cleanInfo(firmsInfoPeople):
    keyName = input("Введіть тип даних, що потрібно ВИДАЛИТИ: ")
    keyValue = input("Введіть значення пошуку: ")

    for item in firmsInfoPeople:
        if item.get(keyName) == keyValue:
           item.clear()
    return print("ІНФО про співробітника видалено!")


cleanInfo(firmsInfoPeople)
print(firmsInfoPeople)



#4
print('-'*20,'#4','-'*20)
dict1 = {"яблуко": 15, "банан": 20, "груша": 18}
dict2 = {"яблуко": 19, "банан": 100, "лимон": 12}


def unDictionary(d1,d2):
    print(dict1,dict2)
    '''для кожного ключа в словнику 1'''
    for key in dict1:
        '''якщо такий ключ є в словнику 2'''
        if key in dict2:
            '''створюємо нові словники зі спільним ключем, де додаються їх значення'''
            dict3={key:dict1[key]+dict2[key]}
            print(dict3)
            '''створюємо словник, де пріоритет надається доданим значенням спільних ключів'''
            dictnew=dict1|dict2|dict3
    return print(dictnew)


unDictionary(dict1, dict2)

#5
print('-'*20,'#5','-'*20)
text='''Підрахунок кількості слів у тексті
        Напишіть програму, яка підраховує кількість
        кожного слова у введеному тексті та зберігає
        цю інформацію в словнику.'''
print(text)



def countWords(text):
    text=text.replace('.','')
    text=text.replace(',','')
    text=text.split()
    print(text)
    texts={}
    for i in text:
        if i not in texts:
             texts[i]=1
        else:
            texts[i]+=1
    for key, val in texts.items():
        print(f"Кількість слова:    {key} = {val}")

    return texts


texts=countWords(text)













