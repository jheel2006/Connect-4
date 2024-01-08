import random
import os
import time

#initializing required variables
NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS=2
board = []
checkers=['X','O','V','M','H']

turn=random.randint(0,NUM_PLAYERS-1)
game_over=False
game_won=False


#making the game board
for row in range(NUM_ROWS):
    row_list = []
    for col in range(NUM_COLS):
        row_list.append(' ')
    board.append(row_list)

#function to print the game board after each turn
def print_board():
    letter = ord('A')
    for col in range(NUM_COLS):
        print('   ' + chr(letter), end='')
        letter += 1

    print("\n +" + "---+" * NUM_COLS)

    for row in range(NUM_ROWS):
        print(' ' + '|', end=' ')
        for col in range(NUM_COLS):
            print(board[row][col] + ' |', end=' ')
        print("\n +" + "---+" * NUM_COLS)

#function to check for 4 checkers in a row horizontally
def horizontal_win(row,col):
    if col+3 in range(NUM_COLS) and board[row][col]==board[row][col+1]==board[row][col+2]==board[row][col+3]:
        global game_won
        global game_over
        game_won=True
        game_over=True
        print('Player '+board[row][col]+' won!')
        return True
    else:
        return False
#function to check for 4 checkers in a row vertically   
def vertical_win(row,col):
    if row+3 in range(NUM_ROWS) and board[row][col]==board[row+1][col]==board[row+2][col]==board[row+3][col]:
        global game_won
        global game_over
        game_won=True
        game_over=True
        print('Player '+board[row][col]+' won!')
        return True
    else:
        return False

#function to check for 4 checkers in a row diagonally    
def diagonal_win(row,col):
    global game_won
    global game_over
    if (row+3 in range(NUM_ROWS) and col+3 in range(NUM_COLS)) or (row+3 in range(NUM_ROWS) and col-3 in range(NUM_COLS)):
        #bottom right to top left
        if (row+3 in range(NUM_ROWS) and col+3 in range(NUM_COLS)) and board[row][col]==board[row+1][col+1]==board[row+2][col+2]==board[row+3][col+3]:
            game_won=True
            game_over=True
            print('Player '+board[row][col]+' won!')
            return True
        #bottom left to top right
        elif (row+3 in range(NUM_ROWS) and col-3 in range(NUM_COLS)) and board[row][col]==board[row+1][col-1]==board[row+2][col-2]==board[row+3][col-3]:
            game_won=True
            game_over=True
            print('Player '+board[row][col]+' won!')
            return True
        else:
            return False

print_board() #printing the board in its initial stage

while game_over==False:
    #asking the player to input a column and checking its validity
    while True:
        column=input('Player '+checkers[turn]+', please enter a column: ' )
        if len(column)==1:
            if ord(column) in range(ord('A'),ord('A')+NUM_COLS):
                break
            else:
                print('Invalid column entered. Please try again')
        else:
            print('Invalid column entered. Please try again')

    #adding the checker to the appropriate spot in the column/checking whether the column is full
    col_index=ord(column)-ord('A')
    turn_lost=True
    for row in board[::-1]:
        if row[col_index]==' ':
            row[col_index]=checkers[turn]
            turn_lost=False
            break
    if turn_lost==True:
        print('This column is already full! You have lost your turn.')
        turn=(turn+1)%NUM_PLAYERS
        continue

    
    os.system("clear") #clears the screen before printing the board    
    print_board() #printing the new board after player chooses a valid column

    #checking for possible win

    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if board[row][col]!=' ':
                #checking for 4 checkers in a row horizontally
                if horizontal_win(row,col):
                    break
                #checking for 4 checkers in a row vertically
                elif vertical_win(row,col):
                    break
                #checking for 4 checkers in a row diagonally 
                elif diagonal_win(row,col):
                    break
                #if there is no combination of 4 checkers in a row, then the program does nothing and continues as usual
                else:
                    pass

        if game_won==True:
            break  
        
    #checking if more turns are possible                
    finished=True
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if board[row][col]==' ':
                finished=False
                break
    
    if finished==True and game_won==False:
        print('The game is a draw')
        game_over=True

    turn=(turn+1)%NUM_PLAYERS