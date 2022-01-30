# X for placing battleship and hit battleship
"""
Symbols used in the Battleships game
"""
# '-' for available space
# '-' for missed shot

from random import randint

player_board = [[' '] * 5 for x in range(5)]
computer_board = [[' '] * 5 for x in range(5)]
computer_hidden_board = [[' '] * 5 for x in range(5)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}


def print_board(board):
    """
    Prints the Battleships playing field
    """
    print('   A B C D E')
    print('   ----------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def populate_board(board):
    """
    Spawns ships on The Battlefield
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 4), randint(0, 4)
        while board[ship_row][ship_column] == '#':
            ship_row, ship_column = randint(0, 4), randint(0, 4)
        board[ship_row][ship_column] = '#'


def computer_guess():
    """
    Computer guess on battleship grid
    """
    ship_row, ship_column = randint(0, 4), randint(0, 4)
    while player_board[ship_row][ship_column] == "X" or player_board[ship_row][ship_column] == "-":
        ship_row, ship_column = randint(0, 4), randint(0, 4)
    return ship_row, ship_column


def get_ship_location():
    """
    Input for Rows and Columns along with some input validation
    """
    row = input(' Please enter a ship row 1 - 5')
    while row not in '12345' or len(row) != 1:
        print('Please enter a valid row')
        row = input(' Please enter a ship row 1 - 5')
    column = input('Please enter a ship column A - E').upper()
    while column not in 'ABCDE' or len(row) != 1:
        print('Please enter a valid column')
        column = input('Please enter a ship column A - E').upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hits(board):
    """
    Counts the number of Battleships hit
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count = + 1
    return count


def main():
    """
    Runs the battleship game
    """
    populate_board(computer_hidden_board)
    populate_board(player_board)
    while count_hits(player_board) < 5 or count_hits(computer_board) < 5:
        print('WELCOME TO BATTLESHIP')
        print_board(computer_board)
        print("COMPUTER BOARD")
        print_board(player_board)
        print("YOUR BOARD")

        row, column = get_ship_location()
        computer_row, computer_column = computer_guess()
        if computer_hidden_board[row][column] == '-':
            print('You already guessed that')
        elif computer_hidden_board[row][column] == '#':
            print(' Congratulations, you have hit the battleship!')
            computer_board[row][column] = 'X'
        else:
            print('Sorry you have missed')
            computer_board[row][column] = '-'
        if count_hits(computer_hidden_board) == 5:
            print('Congratulations, you have sunk all the battleships')
            break

        if player_board[computer_row][computer_column] == '#':
            print('Oops, your battleship was hit!')
            player_board[computer_row][computer_column] = 'X'
        else:
            print('That was a close one, computer missed')
            player_board[computer_row][computer_column] = '-'
        if count_hits(player_board) == 5:
            print('Unlucky, all your battleships have been sunk')
            break

        if count_hits(computer_board) == 5:
            print("Congratulations you won")


if __name__ == "__main__":
    main()
