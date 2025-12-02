#1
def randomnum(num1,num2):
    for i in range(num1,num2+1):
        if i%2==0:
            print(i,end=' ')
    return print()

randomnum(1,100)

#2
def minofnums(*args):
    return print(f'The minimum number is {min(args)}')

minofnums(5,9,3,7,5)

#3
def prodnum(num1,num2):
    if num1 > num2:
       num1,num2=num2,num1
    product=1
    for i in range(num1,num2+1):
        product*=i
    return print(f'The product of nums in diapason is: {product}')

prodnum(9,5)

#4
def countdigitsinnum(num):
    nums = str(num)
    nums=[int(i) for i in nums]
    return print(f'The number of digits in list is: {len(nums)}')

countdigitsinnum(5555)

#5
def palindromeofnum(num):
    num = str(num)
    nums = list(num)
    nums = [int(i) for i in nums]
    nums1 = nums[:len(nums) // 2]
    nums2 = nums[len(nums) // 2:]
    if nums1 == nums2:
        return print(f'number is palindrom?:{True}')
    else:
        return print(f'number is palindrom?:{False}')

palindromeofnum(1233689)

#6
def productofnum(numms):
    product = 1
    for i in numms:
        product *= i
    return print(f'The product of nums in list is: {product}')

numms=[1,2,3,4,5,6,7,8,9]
productofnum(numms)

#7
def mininlistnum(nuums):
    return print(f'The minimum number in list {min(nuums)}')

nuums=[1,2,3,4,5,6,7,8,9]
mininlistnum(nuums)

#8
def primenumbersinlist(nnums):
    primes = []
    for i in nnums:
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            primes.append(i)
    #print(primes, end=' ')
    return print(f'The prime number in list is: {len(primes)}')

nnums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
primenumbersinlist(nnums)

#9
def deletenuminlist(nums1):
    delnum=(int(input('Enter the number to be deleted: ')))
    nums2=[i for i in nums1 if i!=delnum]
    return print(f'The count of deleted number in list is: {len(nums1) - len(nums2)}')


nums1=[1,1,1,1,1,1,1,1,1,1]
deletenuminlist(nums1)


#2class
def randomnum():
    for i in range(1,100):
        if i%2!=0:
            print(i,end=' ')
    print()

randomnum()

#3class
def maxnum(num1,num2,num3,num4):
    return max(num1,num2,num3,num4)
number=maxnum(100,25,3,4)
print(number)

#4class
def primenumber(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    #print(count, end=' ')
    if count <= 2:
        return True
    else:
        return False
num1=primenumber(19)
print(num1)


#5class
def happynumber(num):
    num = str(num)
    nums = list(num)
    nums=[int(i)for i in nums]
    nums1 = nums[:len(nums) // 2]
    nums2 = nums[len(nums) // 2:]
    if sum(nums1) == sum(nums2):
        return True
    else:
        return False

hpn=happynumber(856923)
print(hpn)
