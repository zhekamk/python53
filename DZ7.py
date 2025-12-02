#1
def sumnum(a,b):
    if a>b:
        return 0
    else:
        return a+sumnum(a+1,b)


sumnum1=sumnum(3,5)
print(f'The sum of digits in diapason is: {sumnum1}')

#2
def stars(a):
    if a<=0:
        return ''
    else:
        #return print('*')+print(stars(a-1))
        return '*'+stars(a-1)

stars1=stars(20)
print(stars1)

#3
def square(a):
    return a**2

def cube(a):
    return a**3

def negative(a):
    return -a

def userchoice(c):
    if c=='1':
        return square
    elif c=='2':
        return cube
    elif c=='3':
        return negative

mychoice1=userchoice('3')
print(mychoice1(2))

#4
# list1=[1,2,3]
# list2=[4,5,6]
# list3=[7,8,9]
# print(list1)
# print(list2)
# print(list3)
#
# def choicex(c):
#     global list1
#     global list2
#     global list3
#     if c=='1':
#        list1=['x',2,3]
#     print(list1)
#     print(list2)
#     print(list3)
#     if c=='2':
#        list1=[1,'x',3]
#     print(list1)
#     print(list2)
#     print(list3)
#
#
# xchoice=choicex('2')
# print(xchoice)

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")



