#1
str=input('Введіть текст:')
print(f'Кількість символів включно з пробілами:',len(str))


#2
str1=input('Введіть текст:')
for i in str1:
    print(i)
print()

#3
str2=input('Введіть текст:')
upper=0
for i in str2:
    if i.isupper():
        upper+=1
print(f'Кількість великих літер: {upper}')

#4
str3=input('Введіть текст:')
point=0
for i in str3:
    if i.count(".") or i.count("!") or i.count("?"):
        point+=1
print(f'\nКількість речень в тексті: {point}')

#5
str1=input('Введіть текст:')
str1=str1.replace(' ','')
str1=str1.replace(',','')
str1=str1.replace('.','')
str1=str1.replace('!','')
str1=str1.replace('?','')
str1=str1.replace(';','')
str1=str1.lower()
#print(str1)
str2=str1[::-1]
if str2==str1:
    print("Введений текст є паліндромом")
else:
    print("Введений текст НЕ є паліндромом")

#6
row=input('Введіть текст:')
symb1=input('Введіть перший символ,що присустій в тексті:')
symb2=input('Введіть другий символ,що присустій в тексті:')
row1=row[:row.find(symb1)]
row2=row[row.find(symb2)+1:]
print(row1+row2)











