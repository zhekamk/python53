# #функції
#
# def printMsg():
#     print ('Hello from my first function')
#
#
# printMsg()
# printMsg()
# printMsg()
# printMsg()
#
# print('hello', 'test')
#
#
# def printMsgnew(msg):
#     print (msg)
#
# printMsgnew('new facts')
#
#
# def plusNums(num1, num2, num3):
#     # print (num1 + num2 + num3)
#     return num1+num2+num3
#
#
# sum=plusNums(1,2,3)+10
# print(sum)
# sum=plusNums(1,2,3)
# print(sum)
#
#
# if '2'.isdigit():
#     print('ok')
#
#
# def checfLog(userLog):
#     if userLog=='admin':
#         return userLog.lower()
#     elif userLog=='user':
#         return userLog.upper()
#     else:
#         return 'wrong'
#
# print(checfLog('admin'))
# print(checfLog('user'))
#
#
# def Jobs():
#     print(""""Don't let the noise of others opinions
#     drown out your own inner voice"
#     Steve Jobs""")
#
# Jobs()
#
# def userGreetings(login,passw='admin'):
#     if login == 'admin'and passw == 'admin':
#         print('Welcome admin')
#     elif login == 'student ':
#         print('Welcome student')
#     else:
#         print('Welcome user')
#
# userGreetings('admin')



def sumOfnums(*args):
    print(args)
    return sum(args)

print(sumOfnums(2,2,2,2,2))

# local and global namespase
# number=100
# def multiplynums(num1, num2):
#     # start local namespace
#     global number
#     number=200
#     print(number)
#     return num1*num2
#
#
# multiplynums(2,2)
# print(number)
#
# import random
# #2class
# def randomnum():
#     for i in range(1,100):
#         if i%2!=0:
#             print(i,end=' ')
#     print()
#
# randomnum()
#
# #3class
# def maxnum(num1,num2,num3,num4):
#     return max(num1,num2,num3,num4)
# number=maxnum(100,25,3,4)
# print(number)
#
# #4class
# def primenumber(num):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     #print(count, end=' ')
#     if count <= 2:
#         return True
#     else:
#         return False
# num1=primenumber(19)
# print(num1)
#
#
# #5
# def happynumber(num):
#     num = str(num)
#     nums = list(num)
#     nums=[int(i)for i in nums]
#     nums1 = nums[:len(nums) // 2]
#     nums2 = nums[len(nums) // 2:]
#     if sum(nums1) == sum(nums2):
#         return True
#     else:
#         return False
#
# hpn=happynumber(856923)
# print(hpn)











