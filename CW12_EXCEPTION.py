#Винятки
# print('hello')


#try except
# try:
#     amount=int(input('enter amount-'))
#     items_Type=input('enter items-type')
#     parts_nymber=int(input('enter part-nymber'))
#     parts_amount=amount/parts_nymber
#     print(f'supply of',parts_amount)
# except:
#     print('error')

# try:
#     amount=int(input('enter amount-'))
#     items_Type=input('enter items-type')
#     parts_nymber=int(input('enter part-nymber'))
#     parts_amount=amount/parts_nymber
#     print(f'supply of,{amount},{items_Type}saved')
#
#             except ValueError:
#                 print('error')
#             except ZeroDivisionError:
#                 print('error/0')
#             except Exception:
#                 print('same error')
#             finally:
#                 print('finish')


# try:
#     num=int(input())
#     print(num**2)
# except ValueError:
#     print('error')
# else: #працює якщо немає помилки
#     print('hghj')
# finally:# завжди працює
#     print('finish')


# try:
#     amount=int(input('enter amount-'))
#     items_Type=input('enter items-type')
#     parts_nymber=int(input('enter part-nymber'))
#     parts_amount=amount/parts_nymber
#     print(f'supply of,{amount},{items_Type}saved')
#
# except (ValueError, TypeError):
#        print('error')
# except ZeroDivisionError:
#        print('error/0')
# except Exception as ex:
#        print('same error -,',ex)
# finally:
#        print('finish')

#
# try:
#     salary=int(input("Enter the salary:"))
#     if salary<0:
#         raise Exception("Salary cannot be less than zero")
# except Exception as ex:
#     print('Error',type(ex).__name__, ex)

# print('final price calculating')
# try:
#     price=float(input("Enter start product price:"))
#     discount=float(input("Enter % of discount:"))
#     if discount<0 or discount>100:
#         raise ValueError("Discount cannot be less than zero and>100")
#     finalPrice=price*(1-discount/100)
#     print(f"final price is,{finalPrice:.2f}")
# except ValueError as ex:
#     print('inputError', ex)
# except:
#     print('something went wrong')
# finally:
#     print('calculating finally')


# print('money exchange')
# try:
#     countDol=float(input("Enter count of $:"))
#     exchangeEuro=float(input("Enter cours of exchange Euro:"))
#     if exchangeEuro<0 or exchangeEuro>1:
#         raise ValueError("exchangeEuro cannot be less than zero and>2")
#     finalEuro=countDol*exchangeEuro
#     print(f"final Euro is,{finalEuro:.2f}")
# except ValueError as ex:
#     print('inputError', ex)
# except:
#     print('something went wrong')
# finally:
#     print('excange is finally')

#3
try:
    markStudent=input("Enter marks of students:")
    markStudents=[int(i) for i in markStudent.split()]
    if not markStudents:
         raise ZeroDivisionError("Список порожній")
    averageMark=sum(markStudents)/len(markStudents)
    print(f"середнє значення,{averageMark}")
except ValueError:
    print('введено неправильні значення')
except ZeroDivisionError as e:
    print('something went wrong',e)
finally:
     print('Завершення обчислень')

