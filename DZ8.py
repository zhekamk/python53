#1
nums=[1,2,3,4,5]
#print(nums)
numssquare=list(map(lambda x: x**2, nums))
print(f'#1   {numssquare}')

#2
fruitlasts=['apple','banana','cherry']
#print(fruitlasts)
lenghtfruitnames=list(map(lambda x:len(x),fruitlasts))
print(f'#2   {lenghtfruitnames}')

#3
nums1=[1,2,3,4,5]
nums2=list(filter(lambda x: x%2==0,nums1))
print(f'#3   {nums2}')

#4
fruitAs=list(filter(lambda x:x[0]=='a',fruitlasts))
print(f'#4   {fruitAs}')

#5
nums3=list(filter(lambda x: x%3==0,nums1))
print(f'#5   {nums3}')

#6
numbers=[1,2,3]
numbers1=[4,5,6]
numbers2=list(zip(numbers,numbers1))
print(f'#6   {numbers2}')

#7
productnums=list(map(lambda x,y: x*y,numbers,numbers1))
print(f'#7    {productnums}')

#8
numss=[(1,2), (3, 1), (4, 4), (5, 3)]
numss1=list(filter(lambda x:x[0]>x[1],numss))
print(f'#8    {numss1}')

#9
from random import randint
randomnums=[randint(-100,100) for i in range(20)]
print(f'#9   {randomnums}')
plusnums=list(filter(lambda x:x>0,randomnums))
print(f'#9   List of positive numbers: {plusnums}')

#10
from random import randint
randomnums=[randint(-100,100) for i in range(20)]
print(f'#10   {randomnums}')
numb1=int(input('#10   Enter first number: '))
numb2=int(input('#10   Enter second number: '))
diapasonofnums=list(filter(lambda x:numb1<x<numb2,randomnums))
print(f'#10   List of numbers in diapason: {diapasonofnums}')

#11
randomnums1=[5,5.5,8,9.2,7.0,8.0,2,3,4,7.7,4.4]
print(f'#11   {randomnums1}')
randomnums2=list(filter(lambda x:x==int(x),randomnums1))
print(f'#11   List of integer number:{randomnums2}')

#12
loginlists=[19573,49876,13694,78549,36912,78921,46923]
print(f'#12   Login lists: {loginlists}')
loginlistsS=list(map(lambda x:str(x)+'$',loginlists))
print(f'#12   Login lists with $: {loginlistsS}')

#13
list1=[1,2,3,4,5]
list2=['end','+','=','*','/']
list3=[1,2,3,4,5]
list4=list(zip(list1,list2,list3))
print(f'#13   {list4}')

#14
randomnumss=[randint(-100,100) for i in range(10)]
print(f'#14   {randomnumss}')
randomnumss1=list(map(lambda x:str(x),randomnumss))
print(f'#14   List of str numbers: {randomnumss1}')


