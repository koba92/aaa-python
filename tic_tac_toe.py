import numpy as np
from typing import Iterable

ROW_NAMES=['a','b','c','d','e']

def create_field():
    """Function that creates a gaming field with valid size"""
    while 1==1:
        try:
            n=int(input('Enter field size from 3 to 5: '))
        except:
            n=0
        if (n>=3)&(n<=5):
            field=np.zeros((n,n))
            created=True
            return field
        else:
            print('Incorrect input, try again!')

def num_to_symbol(num: int) -> str:
    """Functions that converts array values into grafic symbols X/O/empty"""
    if num==0:
        return '_'
    elif num==1:
        return 'X'
    else:
        return 'O'

def draw_field(field: Iterable):
    """Functions that draws current field state"""
    print(' |', end='')
    for i in range(len(field)):
            print(str(i+1)+'|',end='')
    print('\r')
    for i in range(len(field)):
        print(ROW_NAMES[i]+'|',end='')
        for j in range(len(field)):
            print(num_to_symbol(field[i][j])+'|',end='')
        print('\r')

def check_move_is_correct(field: Iterable, move: str) -> Iterable:
    """Functions that check whether the move is correct and, 
    if yes, returns also numeric coordinates of chosen point"""
    try:
        row=ROW_NAMES.index(move[0])
        column=int(move[1])-1
    except:
        return [False, -1, -1]
    if (row<0)|(row>=len(field))|(column<0)|(column>=len(field)):
        return [False, -1, -1]
    if field[row,column]!=0:
        return [False, row, column]
    else:
        return [True, row, column]

def get_move(field: Iterable, player_number: int) -> Iterable:
    """Functions requests correct move from a player and returns 
    numeric coordinates of chosen point"""
    while 1==1:
        move=input(f'Player{player_number}, your move: ')
        move_result=check_move_is_correct(field, move)
        if (move_result[0] is False)&(move_result[1]==-1):
            print('Incorrect input, try again!')
            continue
        elif (move_result[0] is False)&(move_result[1]!=-1):
            print('The cell is busy, try again!')
            continue
        else:
            return move_result[1:3]       

def switch_player(current_player: int) -> int:
    """Function switches current player to another"""
    if current_player==1:
        return 2 
    else:
        return 1

def check_rows(field: Iterable, checked_value: int) -> bool:
    """Function checks whether there is a full row 
    of checked value in a field array"""
    for i in range(len(field)):
        result=True
        for j in range(len(field)):
            if field[i, j]!=checked_value:
                result=False
                break
        if result==True:
            return result
    return result

def check_columns(field: Iterable, checked_value: int) -> bool:
    """Function checks whether there is a full column 
    of checked value in a field array"""
    for j in range(len(field)):
        result=True
        for i in range(len(field)):
            if field[i, j]!=checked_value:
                result=False
                break
        if result==True:
            return result
    return result

def check_diag(field: Iterable, checked_value: int) -> bool:
    """Function checks whether there is a full diagonal 
    of checked value in a field array"""
    result=True
    for i in range(len(field)):
        if field[i, i]!=checked_value:
            result=False
    if result==True:
        return result
    else:
        result=True
        for i in range(len(field)):
            if field[i, len(field)-i-1]!=checked_value:
                result=False
    return result

def check_win(field: Iterable, current_player: int) -> bool:
    """Function checks if current player has won the game"""
    win_diag=check_diag(field, current_player)
    win_row=check_rows(field, current_player)
    win_col=check_columns(field, current_player)
    return win_diag|win_row|win_col

def check_draw(field: Iterable) -> bool:
    """Functions checks if it draw"""
    draw=True
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i,j]==0:
                draw=False
    return draw
    
field=create_field()
current_player=1
win=False
draw=False
while not win|draw:
    draw_field(field)
    move=get_move(field, current_player)
    field[move[0],move[1]]=current_player
    win=check_win(field, current_player)
    draw=check_draw(field)
    current_player=switch_player(current_player)
draw_field(field)
current_player=switch_player(current_player)
if win:
    print(f'Player{current_player} won!')
else:
    print('It is draw!')
