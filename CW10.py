# # TUPLE, SET, FROZENSET
#
# userTypes=('admin','student', 'teacher')
# print(type(userTypes))
# print(userTypes)
#
# myEmptTuple=()
# print(type(myEmptTuple))
# print(myEmptTuple)
#
# tuple1=(1,)
# print(type(tuple1))
# print(tuple1)
#
# tuple2=tuple([1,2,3])
# print(tuple2)
#
# itemTuple=('item1','item2','item1', 100,200,300,(1,2,3),[4,5,6])
# print(itemTuple)
# print(itemTuple[-1])
# # del itemTuple
# # print(itemTuple)
#
#
# # print(itemTuple.count('item1'))
# # for i in range(len(itemTuple)):
# #      print(itemTuple[i])
# #
# # tuple3=tuple1+tuple2
# # print(tuple3)
# #
# # def askPersonInfo():
# #     fName=input('Enter first name: ')
# #     lName=input('Enter last name: ')
# #     yearBirth=input('Enter year birth: ')
# #     return fName,lName,yearBirth
# #
# # personInfo=askPersonInfo()
# # print(personInfo)
# #
# # # def askHobby():
# # #     hobby=1
# # #     hobbyList=[]
# # #     while True:
# # #         hobbyName=input('Enter hobby name: ')
# # #         if hobbyName =='':
# # #             print('No info')
# # #             break
# # #         else:
# # #             hobbyList.append(hobbyName)
# # #             hobby=hobby+1
# # #     if len(hobbyList)>0:
# # #         print(f'you have{hobbyList-1} hobby)
# # #     else:
# # #         print('you have no hobby')
# # #     return hobbyList
# #
# # def askAddInfo(querystr):
# #     info=1
# #     infoLists=[]
# #     while True:
# #         infoName=input('Enter hobby name: ')
# #         if infoName =='':
# #             print('No info')
# #             break
# #         else:
# #             infoLists.append(infoName)
# #             info+=1
# #         if len(infoLists)>0:
# #             if querystr=='hobby':
# #                 print(f'you have {infoLists-1} hobby')
# #             elif querystr == 'program':
# #                 print(f"you have {infoLists-1} program")
# #             else:
# #                 print('you have no hobby')
# #         return infoLists
# #
# #
# # infoLists=[]
# # infoLists.append(askPersonInfo())
# # infoLists.append(askAddInfo('hobby'))
# # print(infoLists)
#
# # set
#
# mySet1={1,2,3,3}
# mySet2={'Joe','Bob','Bill'}
# mySet3={23,'Joe', True}
# print(mySet1)
# print(mySet2)
#
# myList=['111',('222','333')]
# print(set(myList))
#
# marks1={8,9,8}
# marks2={9,8,8}
# print(marks1==marks2)
#
# for item in mySet2:
#     print(item, end='--')
# print()
#
# word='some letter'
#
# for letter in set(word):
#     print(letter, end=' ')
# print()
#
# meSet={1,2,3}
# print(meSet)
# meSet.add(4)
# print(meSet)
# meSet.update([3,4,5])
# print(meSet)
# meSet.remove(5)
# print(meSet)
# meSet.discard(44)
# print(meSet)
# meSet.pop()
# print(meSet)
#
# oldUsers={'user1','user2','user3'}
# newUsers={'user3','user4','user5'}
# print(oldUsers)
# print(newUsers)
# print('intersection of users')
# print(oldUsers.intersection(newUsers))
# print(oldUsers&newUsers)
# print('union of users')
# print(oldUsers.union(newUsers))
# print(oldUsers|newUsers)
# print('difference of users')
# print(oldUsers.difference(newUsers))
# print(newUsers.difference(oldUsers))
#
# # frozenset()
# frozenA=frozenset({'user1','user2','user3'})
# print(frozenA)
# frozenset

#1
print('-'*20,'#1','-'*20)
fruits=('apple','banana','orange','apple','orange','apple')
fruit=input('enter fruit:')
fruit1=fruits.count(fruit)
print(f'Count of {fruit} is: {fruit1}')

#2
print('-'*20,'#2','-'*20)
fruits=('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
fruit=input('enter fruit:')
countfruit=0
for i in fruits:
    if fruit in i:
        countfruit += 1
print(f'Count of {fruit} is: {countfruit}')

#3
print('-'*20,'#3','-'*20)
number = input("Enter numbers using space: ")
numbers=number.split()
numbers=[int(i) for i in numbers]
numbers=set(numbers)
print(f'list of nambers without repeating:{numbers}')

#4
print('-'*20,'#4','-'*20)
studentPythons=['Bob','Jane','John','Smith','Sandra']
studentJavas=['Bob','Nik','John','Smith','Linda']
studentPythons=set(studentPythons)
print(studentPythons)
studentJavas=set(studentJavas)
print(studentJavas)
print(f'Students learn Python and Java: {studentPythons&studentJavas}')
print(f'Students learn only Python: {studentPythons.difference(studentJavas)}')
print(f'Students learn only Java: {studentJavas.difference(studentPythons)}')
















