#1
print('-'*20,'#1','-'*20)
from random import randint
randomnums1=[randint(1,20) for i in range(5)]
randomnums1=tuple(randomnums1)
print(f'tuple1: {randomnums1}')
randomnums2=[randint(1,20) for i in range(5)]
randomnums2=tuple(randomnums2)
print(f'tuple2: {randomnums2}')
randomnums3=[randint(1,20) for i in range(5)]
randomnums3=tuple(randomnums3)
print(f'tuple3: {randomnums3}')
randomnums1=set(randomnums1)
randomnums2=set(randomnums2)
randomnums3=set(randomnums3)
print(f'Unique number for tuple1: {randomnums1-randomnums2-randomnums3}')
print(f'Unique number for tuple2: {randomnums2-randomnums1-randomnums3}')
print(f'Unique number for tuple3: {randomnums3-randomnums2-randomnums1}')

#2
print('-'*20,'#2','-'*20)
from random import randint
randomnums1=[randint(1,5) for i in range(5)]
randomnums1=tuple(randomnums1)
print(f'tuple1: {randomnums1}')
randomnums2=[randint(1,5) for i in range(5)]
randomnums2=tuple(randomnums2)
print(f'tuple2: {randomnums2}')
randomnums3=[randint(1,5) for i in range(5)]
randomnums3=tuple(randomnums3)
print(f'tuple3: {randomnums3}')
rnums=list(zip(randomnums1, randomnums2, randomnums3))
print(rnums)
for i1,i2,i3 in rnums:
    if i1==i2==i3:
        print(f'Same elements in column:{i1}')

#3
print('-'*20,'#3','-'*20)
from random import randint
randomn=[randint(1,199) for i in range(20)]
randomn=tuple(randomn)
print(f'tuple of numbers: {randomn}')
count1=0
count2=0
count3=0
print(len(randomn))
for i in randomn:
    if len(str(i))==1:
        count1+=1
    elif len(str(i))==2:
        count2+=1
    elif len(str(i))==3:
        count3+=1
print(f'count of single-digit number: {count1}')
print(f'count of double-digit number: {count2}')
print(f'count of triple-digit number: {count3}')

#4
print('-'*20,'#4','-'*20)
listNameAge=[("Ганна", 22), ("Іван", 16), ("Марія", 20), ("Петро", 25)]


def listNameAge18(list):
    list18 = []
    for item in list:
        if item[1]>18:
            list18.append(item[0])
    return list18


newlistNameAge=listNameAge18(listNameAge)
print(*newlistNameAge)

#5
print('-'*20,'#5','-'*20)
listGoods=[('Яблука', 10), ('Молоко', 5), ('Хліб', 3), ('Масло', 2)]


def countOfGoods(list):
    sum = 0
    for item in list:
        sum+=item[1]
    return  (f'Загальна кількість товарів: {sum}')


countOfGoods1=countOfGoods(listGoods)
print(countOfGoods1)

#6
print('-'*20,'#6','-'*20)
listBooks=[('Майстер і Маргарита', 'Михайло Булаков', 1967),
           ('Злочин і покарання', 'Федор Достоєвський', 1866),
           ('Війна і мир', 'Лев Толстой', 1869),
           ('Війна і мир', 'Лев Толстой', 1869),
           ('1984', 'Джордж Оруелл', 1949),
           ('1984', 'Джордж Оруелл', 1949)]
print(listBooks)


def authorsOfBooks(list):
    print(f'Список авторів без повторів:\n')
    listAuthors=set()
    for i in list:
        listAuthors.add(i[1])
    for i in listAuthors:
        print(i)
    return listAuthors


authorsOfBooks(listBooks)




    










