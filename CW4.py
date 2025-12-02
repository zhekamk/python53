myStr = "hello"
print(type(myStr))
print(myStr)

myStr2 = 'hello'
print(myStr2)

myStr3 = '''
some
text
'''

userSms = "python пайтон"
userSmsEncode = userSms.encode('utf-8')

userSmsDec = userSmsEncode.decode('utf-8')

print(userSms, "==", userSmsEncode)

print(id(myStr))
myStr = "new text"
print(id(myStr))

myStr = "python"
print(myStr)
print(myStr[0])
print(myStr[1])
print(myStr[len(myStr) - 1])
print(len(myStr))
print(myStr[- 1])

str1 = "hello"
str2 = " admin"
print(str1 + str2)  # concat

print(str1 * 3)

# методи зміни регістру рядка
str1 = "python cool tt python"
print(str1)
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.capitalize())
print(str1.swapcase())

# методи пошуку підрядка в рядку
print(str1.count("i"))
print(str1.count("python", 10))

print(str1.find('python'))
print(str1.rfind('python'))

print(str1.index("tt"))
print(str1.rindex('tt'))

# методи перевірки рядків
print(str1.endswith("python"))
print(str1.startswith("python2"))
testStr = 'qweAS123'
print(testStr.isdigit())
print(testStr.isalpha())
print(testStr.isalnum())
print(testStr.islower())

# методи форматування

print(str1.center(50, "*"))
testSpace = "   space   "
print(testSpace.lstrip())
print(testSpace.rstrip())
print(testSpace.strip())

myStr = 'python cool!'
print(myStr)
print(myStr[0:6])
print(myStr[7:12])
print(myStr[7:])
print(myStr[:-1])
print(myStr[-1:])

print(myStr[0:10:2])
print(myStr[:len(myStr) // 2])

print(f"str1: {str1}, str2: {str2}")

userStr = "python123"
digits = 0
letters = 0

for s in userStr:
    if s.isdigit():
        digits += 1
    elif s.isalpha():
        letters += 1


print(f"digits: {digits}")
print(f"letters: {letters}")

# Завдання 2
# Користувач вводить з клавіатури рядок і символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається шуканий символ. Отримане число виведіть на екран.














