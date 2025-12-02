def say_hello():
    name='qwerty'
    print(f'Hello {name}')

print(type(say_hello))

greeting = say_hello
greeting()

customers=['adminJane','adminBob','studnick','stalice','kate']
def sayhelloforclirnt(customer):
    if customer.find('admin')!=-1:
        print(f'hellj admin- {customer}')
    elif customer.find('studnick')!=-1:
        print(f'hellj studnick- {customer}')
    else:
        print(f'hellj - {customer}')


def greeting(customerlist,greetfunc):
    if isinstance(customerlist,list):
        for customer in customerlist:
            greetfunc(customer.lower())

greeting(customers,sayhelloforclirnt)


def calculatesum(a,b):
    return a+b


def calculatemin(a,b):
    return a-b

def calculatemax(a,b):
    if b!=0:
        return a/b


def userchoice(c):
    if c=='1':
        return calculatesum
    elif c=='2':
        return calculatemin
    elif c=='3':
        return calculatemax

mycalculation=userchoice('1')
print(mycalculation(2,2))


#рекурсія -функція яка викликає сама себе

def factorialcalculation(num):
    if num==0:
        return 1
    else:
        print(num, end=' ')
        return num*factorialcalculation(num-1)  #5*4*3*2*1


print(factorialcalculation(10))


def isstrpalindrom(mystr):
    if len(mystr)==0:
        return True
    else:
        if mystr[0]==mystr[-1]:
            print(mystr[1:-1])
            return isstrpalindrom(mystr[1:-1])
        else:
            return False

str1=('madam')
print(isstrpalindrom(str1))

def findmin(numberlist):
    if len(numberlist)>1:
        return min(findmin(numberlist[:-1]), numberlist[-1])
    else:
        return numberlist[0]


num=[2,4,1,8,10]
print('min', findmin(num))


#1
def sumculation(num):
    if num<10:
        return 1
    else:
        return num%10+sumculation(num//10)


print(sumculation(123))

#2
def printnumbers(nums):
     if not nums:
        return
     else:
        print(nums[0], end=' ')
        printnumbers(nums[1:])


nums=[3,7,2,8]
print(printnumbers(nums))


# #3
# def say_hello():
#     return print('Hello')
#
# greeting = say_hello
# greeting()
#
# #4
# def square(a):
#     return a**2
#
# def cube(a):
#     return a**3
#
# def negative(a):
#     return -a
#
# def userchoice(c):
#     if c=='1':
#         return square
#     elif c=='2':
#         return cube
#     elif c=='3':
#         return negative
#
# mychoice1=userchoice('3')
# print(mychoice1(2))






