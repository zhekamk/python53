#lamda - анонімна функція
# lamda аргумент1, аргумент2: вираз
from CW4 import digits


def add10(x):
    return x + 10

nums=[1,2,3,4,5]
for num in nums:
    print(add10(num))

for num in nums:
    print((lambda x: x+10)(num))

students=[['Bob', 70],
        ['Jane', 80],
        ['Piter', 60]]

print(students)

sortedstudeunts=sorted(students, key=lambda x: x[1])
print(sortedstudeunts)

grntodoll=42
discont=0.15
pricedol=lambda x:x/grntodoll*(1-discont)

price=4200
print(f'price: {pricedol(price)} $')
print(f'price: {pricedol(3500)} $')


userName=lambda firstname, lastname: f'full name: {firstname.title()} {lastname.title()}'
print(userName('jane', 'piter'))
#
# num = int(input('Enter a number: '))
# print((lambda x: x**2)(num))

num1=(lambda a,b: max(a,b))
print(num1(1,9))

num2=(lambda a: a%2==0)
print(num2(9))


# функції вишого порядку
studyears=[2000,1997,2002,1999]
print(studyears)
studAges=list(map(lambda x:2025-x, studyears))
# print(studAges)
# for year in studyears:
#     studAges.append(2025-year)
print(studAges)

def makeLog(userName,maker):
    return maker(userName)

def namUpper(name):
    return 'user'+name.upper()

def namLower(name):
    return 'user'+name.lower()

print(makeLog('adm',namLower))

# map() filter() zip()

userLogs=['admin', 'student', 'qwerty','USER']
print(userLogs)

userlogLow=list(map(str.lower,userLogs))
print(userlogLow)

values=['2.3','12','45.34','3']
print(values)

numbers=list(map(float,values))
print(numbers)


digits=list(map(lambda x: int(x[0]),values))
print(digits)
print(digits)

nums1=[10,20,30]
nums2=[1,2,3]
result=list(map(lambda a,b: a**b, nums1, nums2))
print(result)


prices=[100,33,67,99,45]
expensive=list(filter(lambda x:x>50,prices))
print(prices)
print(expensive)

userpass=['1111','sfssf','3232']

for log, password in zip(userLogs, userpass):
    print(f'login:{log}, password: {password}')

print(list(zip(userLogs, userpass)))



















