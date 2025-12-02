#1
num=input("Enter any one five numbers:")
nums=list(num)
print(nums)
print(nums[0:1])
print(nums[4:5])

#2
numbers = [3, 7, 2, 9, 4]
print(f'max of element:{max(numbers)}')
print(f'min of element:{min(numbers)}')
print(f'sum of element:{sum(numbers)}')

#3
word=input("Enter word using space:")
words=word.split()
for i in words:
    print(i)

#4
fruits = ["apple", "banana", "orange"]
print(fruits)
fruits.append(input('Enter your fruit: '))
print(fruits)

#5
nums = [2, 4, 6, 8, 10]
print(nums)
nums[1]=100
print(nums)

#6
number1 = input("Enter a number using space: ")
numbers1=number1.split()
numbers1=[int(i) for i in numbers1]
numbers1=[i for i in numbers1 if i%2==0]
print(numbers1)

#7
number2 = input("Enter 10 numbers using space: ")
numbers2=number2.split()
print(numbers2[::-1])

#8
letters = ['a', 'b', 'c', 'd']
letters.pop(len(letters)-1)
print(letters)

#9
nums = [1, 1, 2, 3, 3, 3, 4]
print(nums.count(3))

#10
number3 = input("Enter 7 numbers using space: ")
numbers3=number3.split()
numbers3=[int(i) for i in numbers3]
print(f'average of element:{sum(numbers3)/len(numbers3)}')

#11
from random import randint
randomnums=[randint(-100,100) for i in range(10)]
print(f'List of random numbers:{randomnums}')
randomnums1=[i for i in randomnums if i>0]
print(f'min of positive element:{min(randomnums1)}')
randomnums2=[i for i in randomnums if i<0]
print(f'max of negative element:{max(randomnums2)}')
print(f'count of negative element:{len(randomnums2)}')
print(f'count of positive element:{len(randomnums1)}')
randomnums3=[i for i in randomnums if i==0]
print(f'count of zero:{len(randomnums3)}')


#2class
number4 = input("Enter numbers using space: ")
number5= int(input("Enter any one number from list: "))
numbers4=number4.split()
numbers4=[int(i) for i in numbers4]
print(f'{numbers4.count(number5)} times the number is given in the list')








