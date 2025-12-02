from unicodedata import category

num1=10
num2=20
num3=30

# LIST - списки

numbers=[num1,num2,num3]
print(numbers)
print(type(numbers))

courses = list(('Meth','design','blogging'))
print(courses)

elements=[123, 'djon', True, 3.14]
print(elements)

list1=[i for i in range(1,11)]
print(list1)

print(elements[0])
print(len(elements))

print(list1[:len(list1)//2])
print(list1[len(list1)//2:])
print(list1[:-1])

# change element in list

marks=[10,2,9,11,8]
print(marks)
marks[1]=10
print(marks)

marks=[]

# python metods for list

prices = [100,234,567,44,24,6,99]
print(f'count of element:{len(prices)}')
print(f'sum of element:{sum(prices)}')
print(f'average of element:{sum(prices)/len(prices)}')
print(f'max of element:{max(prices)}')
print(f'min of element:{min(prices)}')
print(f'sorted of element:{sorted(prices)}')

category1=['drama', 'comedy']
category2=['action']
print(category1+category2)
print(category1*2)

# methods of list
categoryes=category1+category2
print(categoryes)
categoryes.append('fantasy')
print('add fantasy')
print(categoryes)
categoryes.insert(0,'horror',)
print(categoryes)
categoryes.extend(category1)
print(categoryes)

# del
categoryes.pop()
print(categoryes)
categoryes.pop(1)
print(categoryes)
categoryes.remove('drama')
print(categoryes)
# categoryes.clear('comedy')
# print(categoryes)
if 'horror' in categoryes:
    print(categoryes.index('horror'))

print(categoryes.count('fantasy'))
categoryes.sort(reverse=True)
categoryes.reverse()
print(categoryes)

newcats=categoryes.copy()
categoryes.pop()
print(newcats)

studScorse=[['bob',11,6,8,12],
            ['jane', 4,6,7,9],
            ['john',5,6,8,10]]
print(studScorse)

for cat in categoryes:
    print(cat)
for cat in studScorse:
    print(cat)









