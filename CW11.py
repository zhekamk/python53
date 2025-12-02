# nums = [1, 2, 3]
# print(nums[0])
#
# student_info = ["Bob", 19, 11]
# print(f"Name: {student_info[0]}")
#
# st_info_dict = {"name": "Bob",
#                 "age": 19,
#                 "avg_mark": 11}
#
# print(st_info_dict)
# print(type(st_info_dict))
#
# bookDict = {
#     'auther': 'Gvido van Rossum',
#     'title': 'Python course',
#     'price': 230,
#     'pages': 230
# }
#
# print(bookDict)
#
# myDict1 = dict([("a", 111), ('b', 222), ('c', 333)])
# print(myDict1)
#
# keyList = ['a', 'b']
# valueList = [111, 222]
# myDict2 = dict(zip(keyList, valueList))
# print(myDict2)
#
# myDict3 = dict(firstName="Bill", lastName="Geits")
# print(myDict3)
#
# emptyDict = {}
# emptyDict['newKey'] = 111
# emptyDict['newKey'] += 222  # update value in dict
#
# print(emptyDict)
#
# print(len(bookDict))
#
# print(bookDict)
# # newKey = input("Enter new prop of book - ")
# #
# # if newKey not in bookDict:
# #     bookDict[newKey] = input("Enter new value - ")  # add new key with value
#
# # print(bookDict['language'])
#
# for key in bookDict:
#     print(f"{key}: {bookDict[key]}")
#
# print(bookDict.items())
# for key, value in bookDict.items():
#     print(key, value)
#
# print(bookDict.get('title2', "start"))
# # print(bookDict['title2'])
#
# bookDict.update([('reading age', 20), ('online', False)])
# print(bookDict)
#
# # del bookDict
# # bookDict.clear()
#
# print(bookDict.values())
# print(bookDict.keys())
# print(bookDict.pop("title"))  # del item by key or error
#
# print(bookDict.popitem())
# print(bookDict.popitem())
#
# print(bookDict)

users = [
    {'name': 'user1', 'age': 10, 'login': 'qwe213'},
    {'name': 'user3', 'age': 13, 'login': 'ADF1212'},
    {'name': 'user6', 'age': 16, 'login': 'ASDGADF3212'},
    {'name': 'user0', 'age': 18, 'login': 'dgfdf33'},
    {'name': 'user5', 'age': 19, 'login': 'qweasd'}
]

keyName = input("Enter info type: ")
keyValue = input("Enter info value: ")


def find_user(users, keyName, keyValue):
    keyValue = keyValue if keyName != 'age' else int(keyValue)
    for user in users:
        if user.get(keyName) == keyValue:
            print("Element is found !")
            for key, val in user.items():
                print(f"{key}: {val}")
            return user
    return "Element is not found"


myUser = find_user(users, keyName, keyValue)
print(myUser)

sortedUsers = sorted(users, key=lambda x: x['age'])
print(sortedUsers)
