#1
print('-'*20,'#1','-'*20)

try:
    file1lists = ['яблуко\n', 'банан\n', 'груша\n', 'диня\n', 'кокос\n']
    with open('file1.txt', 'w',encoding='utf-8') as file1:
        file1.writelines(file1lists)
    file2lists = ['слива\n', 'банан\n', 'малина\n', 'диня\n', 'вишня\n']
    with open('file2.txt', 'w',encoding='utf-8') as file2:
       file2.writelines(file2lists)
    with open('file1.txt','r',encoding='utf-8') as file1:
        data1=file1.readlines()
        data1s=set(data1)
        print(data1s)
    with open('file2.txt','r',encoding='utf-8') as file2:
        data2=file2.readlines()
        data2s=set(data2)
        print(data2s)
        data3=data1s&data2s
        print(data3)
        data3=list(data3)
        print(data3)
    with open('file1.txt', 'w',encoding='utf-8') as file1, open('file2.txt', 'w',encoding='utf-8') as file2:
        file1.writelines(data3)
        file2.writelines(data3)

except FileNotFoundError as ex:
    print(ex)

#2
print('-'*20,'#2','-'*20)
try:
    file3lists = ['яблуко\n', '123\n', 'груша\n', '156\n', 'кокос\n']
    with open('file3.txt', 'w',encoding='utf-8') as file1:
        file1.writelines(file3lists)
    with open('file3.txt', 'r', encoding='utf-8') as file3, open('file4.txt', 'w', encoding='utf-8') as file4:
        data5 = file3.read()
        print(data5)
        count_symb=len(data5.replace('\n',''))
        #print(count_symb)
        file4.write(f'Кількість символів у file3.txt: {str(count_symb)}\n')
    with open('file3.txt', 'r', encoding='utf-8') as file3, open('file4.txt', 'a', encoding='utf-8') as file4:
        data5 = file3.readlines()
        #print(data5)
        count_row=len(data5)
        #print(count_row)
        file4.write(f'Кількість рядків у file3.txt: {str(count_row)}\n')
    with open('file3.txt', 'r', encoding='utf-8') as file3, open('file4.txt', 'a', encoding='utf-8') as file4:
        data6 = file3.read()
        #print(data6)
        A=['а','о','у','и','і','ї','я','ю','є','е']
        count_A=data6.replace('\n','')
        count_A1=0
        for i in count_A:
            if i in A:
                count_A1+=1
        #print(count_A1)
        file4.write(f'Кількість голосних літер у file3.txt: {str(count_A1)}\n')
    with open('file3.txt', 'r', encoding='utf-8') as file3, open('file4.txt', 'a', encoding='utf-8') as file4:
        data6 = file3.read()
        #print(data6)
        count_B=data6.replace('\n','')
        count_B1=0
        for i in count_B:
            if i.isalpha() and i not in A:
                count_B1+=1
        #print(count_B1)
        file4.write(f'Кількість приголосних літер у file3.txt: {str(count_B1)}\n')
    with open('file3.txt', 'r', encoding='utf-8') as file3, open('file4.txt', 'a', encoding='utf-8') as file4:
        data6 = file3.read()
        #print(data6)
        count_dig=0
        for i in count_B:
            if i.isdigit():
                count_dig+=1
        #print(count_dig)
        file4.write(f'Кількість цифр у file3.txt: {str(count_dig)}\n')
    with open('file4.txt', 'r', encoding='utf-8') as f:
        f = f.read()
        print(f)
except FileNotFoundError as ex:
    print(ex)

#3
print('-'*20,'#3','-'*20)

try:
    file4lists = ['яблуко\n', '123\n', 'груша\n', '156\n', 'кокос\n']
    with open('fil.txt', 'w',encoding='utf-8') as fil:
        fil.writelines(file4lists)
    with open('fil.txt', 'r', encoding='utf-8') as fil, open('fil1.txt', 'w', encoding='utf-8') as fil1:
        dataf = fil.readlines()
        print(dataf)
        dataf1 = dataf.pop()
        print(dataf)
        fil1.writelines(dataf)
    with open('fil1.txt', 'r', encoding='utf-8') as f1:
        f1 = f1.read()
        print(f1)
except FileNotFoundError as ex:
    print(ex)

#4
print('-'*20,'#4','-'*20)
try:
     file6lists = ['яблуко яблуко\n', '123\n', 'груша\n', '156\n', 'кокос\n']
     with open('fil6.txt', 'w',encoding='utf-8') as fil6:
         fil6.writelines(file6lists)
     with open('fil6.txt', 'r', encoding='utf-8') as fil6:
         nlist = fil6.readlines()
         nlist1= list(map(str.strip, nlist))
         nlist2= list(map(lambda x: len(x)-1, nlist))
         max_row=max(nlist2)
         print(nlist1)
         print(nlist2)
         print(max(nlist2))
     with open('fil6.txt', 'a', encoding='utf-8') as f7:
         f7.writelines(f'Довжина найдовшого рядка: {(str(max_row))}')
except FileNotFoundError as ex:
     print(ex)

#5
print('-'*20,'#5','-'*20)

try:
     file8lists = ['яблуко\n','яблуко\n', 'слива\n', 'груша\n', 'груша\n', 'кокос\n','яблуко\n', 'слива\n', 'груша\n']
     with open('fil8.txt', 'w', encoding='utf-8') as f8:
          f8.writelines(file8lists)
     with open('fil8.txt', 'r', encoding='utf-8') as f8:
          data8 = f8.readlines()
          print(data8)
          data8 = list(map(str.strip, data8))
          print(data8)
          word = input('Введіть слово із тексту: ')
          countWord=0
          for i in data8:
              if i==word:
                 countWord += 1
          if countWord>0:
              print(f'Кількість слова ({word}) у тексті: {countWord}')
          else:
              print('Введене слово відсутнє у тексті')
except Exception as ex:
    print(ex)


#6
print('-'*20,'#6','-'*20)

try:
     file9lists = ['яблуко\n','яблуко\n', 'слива\n', 'груша\n', 'груша\n', 'кокос\n','яблуко\n', 'слива\n', 'груша\n']
     with open('fil9.txt', 'w', encoding='utf-8') as f9:
          f9.writelines(file9lists)
     with open('fil9.txt', 'r', encoding='utf-8') as f9:
          data9 = f9.read()
          print(data9)
     with open('fil9.txt', 'r', encoding='utf-8') as f9:
          data9 = f9.readlines()
          #print(data9)
          data9 = list(map(str.strip, data9))
          #print(data9)
          word1 = input('Введіть слово із тексту, яке потрібно замінити: ')
          if word1 not in data9:
              raise ValueError('Такого слова немає в тексті!')
          wordchange=input('Введіть слово, на яке потрібно замінити:')
          newdata=[]
          for i in data9:
              if i!=word1:
                  newdata.append(i)
              else:
                  newdata.append(wordchange)
          #print(newdata)
          newdata = list(map(lambda x: x+'\n', newdata))
          with open('fil9.txt', 'w', encoding='utf-8') as f9:
              f9.writelines(newdata)
          with open('fil9.txt', 'r', encoding='utf-8') as f10:
              data10=f10.read()
              print(f'Новий текст:\n{data10}')
except ValueError as a:
    print(f'Помилка!,{a}')
except Exception as ex:
    print(ex)




