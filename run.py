#X for placing battleship and hit battleship
# '-' for available space
# '-' for missed shot

from random import randint

player_board = [[' '] * 5 for x in range(5)]
computer_board = [[' '] * 5 for x in range(5)]

letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}

def print_board(board):
    print('   A B C D E')
    print('   ----------')
    row_number = 1 
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def populate_board(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,4), randint(0,4)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,4), randint(0,4)
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    row = input(' Please enter a ship row 1 - 5')
    while row not in '12345':
        print('Please enter a valid row')
        row = input(' Please enter a ship row 1 - 5')
    column = input('Please enter a ship column A - E').upper()
    while column not in 'ABCDE':
        print('Please enter a valid column')
        column = input('Please enter a ship column A - E').upper()
    return int(row) - 1, letters_to_numbers[column]

def count_hits(board):
    count = 0 
    for row in board:
        for column in row:
            if column == 'X':
                count =+ 1
    return count

populate_board(player_board)
turns = 10
while turns > 0:
    print('WELCOME TO BATTLESHIP')
    print_board(computer_board)
    row, column = get_ship_location()
    if computer_board [row][column] == '-':
        print('You already guessed that')
    elif computer_board[row][column] == 'X':
        print(' Congratulations, you have hit the battleship!')
        computer_board[row][column] = 'X'
        turns -= 1
    else: 
        print('Sorry you have missed')
        computer_board[row][column] = '-'
        turn -= 1
    if count_hits(computer_board) == 5:
        print('Congratulations, you have sunk all the battleships')
        break
    print('You have' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Sorry, you ran out of turns the game is over')
        break
