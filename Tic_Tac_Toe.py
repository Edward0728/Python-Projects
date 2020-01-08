#Test Version 3

#!/usr/bin/python

game = 0
num = [1,2,3,4,5,6,7,8,9]
board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
win = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
print(f'{board[7]}|{board[8]}|{board[9]}');
print(f'{board[4]}|{board[5]}|{board[6]}');
print(f'{board[1]}|{board[2]}|{board[3]}');
playerA = set()
playerB = set()

while game==0:
    A = int(input('Player A, please enter your step number: '))
    while (A not in num) or (A in playerB):
         A = (input('Player A, please  enter your step number(1-9): ')   
    board[A]='O'
    playerA.add(a)
              


    print(f'{board[7]}|{board[8]}|{board[9]}');
    print(f'{board[4]}|{board[5]}|{board[6]}');
    print(f'{board[1]}|{board[2]}|{board[3]}');

    B = int(input('Player B, please enter your step number: '))
    board[B]='X'
    playerB.add(B)
    print(f'{board[7]}|{board[8]}|{board[9]}');
    print(f'{board[4]}|{board[5]}|{board[6]}');
    print(f'{board[1]}|{board[2]}|{board[3]}');
    x = range(8)
    
    
    for n in x:
        if playerA >= win[n]:
            print('A win!')
            game = 1
            break
        elif playerB >= win[n]:
            print('B win!')
            game = 1
            break

else:
    print('Game Over')