import random


def display_board(board):
    print(' ' + board[7] + '| ' + board[8] + '| ' + board[9])
    print('--------')
    print(' ' + board[4] + '| ' + board[5] + '| ' + board[6])
    print('--------')
    print(' ' + board[1] + '| ' + board[2] + '| ' + board[3])
# Choosing side by first player


def x_or_o():
    global first_input
    name = True
    while name:
        first_input = input("{}, please choose X or O: ".format(Player1_name))
        first_input = first_input.upper()
        if first_input == "X" or first_input == "O":
            print('\n')
            print("Thanks for choosing {}, {} will have another symbol".format(first_input, Player2_name))
            name = False
        elif first_input != "X" or first_input != "O":
            print('\n')
            print("Wrong character, options available: X or O")

    return first_input


# function that assign second mark to the second player
def func_second_player_option():
    global first_player_option
    global second_player_option
    first_player_option = first_input
    if first_player_option == "X":
        second_player_option = "O"
    elif first_player_option == "O":
        second_player_option = "X"


# Asking for the start
def asking_for_the_start():
    stat = True
    while stat:
        start = input("Are you ready to start the game? Type Yes or No: ")
        start = start.upper()
        if start == "NO":
            print('\n')
            print("See you next time")
            stat = False
        elif start == "YES":
            print('\n')
            print("Great, let`s start")
            stat = False
        elif start != "NO" or start != "YES":
            print('\n')
            print("Wrong character, options available: Yes or No")


# function that assign marker to the position
def place_marker(board, marker, position):
    board[position] = marker
    return board


# function that takes from player input
def enter_position():
    integer = True
    while integer:
        position = (input("{} your symbol on the board (1-9): ".format(Player1_name)))
        if position in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = (int(position))
            integer = False
            return position

        else:
            print("Wrong symbol")


def enter_position2():
    integer = True
    while integer:
        position = (input("{} your symbol on the board (1-9): ".format(Player2_name)))
        if position in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = (int(position))
            integer = False
            return position

        else:
            print("Wrong symbol")


# Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. *
# Win check mark should be X or O


def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[7] == marker and board[5] == marker and board[3] == marker))


# Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    return board[position] == " "


# Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    return ((board[1] != " ") and
            (board[2] != " ") and
            (board[3] != " ") and
            (board[4] != " ") and
            (board[5] != " ") and
            (board[6] != " ") and
            (board[7] != " ") and
            (board[8] != " ") and
            (board[9] != " "))


# Write a function that asks the player if they want to play again.

def replay():
    choise = True
    while choise:
        ask = input("Do you want to play again ( Yes or No): ")
        ask = ask.upper()
        if ask == "NO":
            print('\n'*50)
            print("See you next time")
            choise = False
            return False
        elif ask == "YES":
            print('\n')
            print("Great, let`s start")
            choise = False
            return True
        elif ask != "NO)" or ask != "YES":
            print('\n')
            print('Wrong character, options available: Yes or No')


# function with game
def game():
    print("Lets randomly decide who will be first")
    players = [Player1_name, Player2_name]
    first_turn = random.choice(players)
    print("{} will go first".format(first_turn))

    new_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(new_board)
    game_on = True
    # First player turn
    while game_on:
        while first_turn == Player1_name:
            position = enter_position()
            if space_check(new_board, position):
                place_marker(new_board, first_player_option, position)
                print('\n'*10)
                print(display_board(new_board))
                if win_check(new_board, first_player_option):
                    print("{} winner winner chicken dinner".format(Player1_name))
                    game_on = False
                    break
                elif full_board_check(new_board):
                    print("Game is Brawl")
                    game_on = False
                    break
                first_turn = Player2_name

        while first_turn == Player2_name:
            position = enter_position2()
            if space_check(new_board, position):
                place_marker(new_board, second_player_option, position)
                print('\n'*10)
                print(display_board(new_board))
                first_turn = Player1_name
                if win_check(new_board, second_player_option):
                    print("{} winner winner chicken dinner".format(Player2_name))
                    game_on = False
                elif full_board_check(new_board):
                    print("Game is Brawl")
                    game_on = False
    if replay():
        game()
    else:
        print("Thanks for playin`")


# ================================================================================================================================================================================
# ================================================================================================================================================================================
# names of the players
print("Welcome to Andrew`s game")
Player1_name = input("Give me fist player`s name: ")
print('\n')
print("Great " + Player1_name + ", let`s see your opponent ")
Player2_name = input("I`m waiting for the second name: ")
print('\n')
print("Thank you")

# Calling our function to know what symbol is used by who
first_input = ""
x_or_o()

first_player_option = ""
second_player_option = ""
func_second_player_option()
mark = first_player_option
mark2 = second_player_option
print(Player1_name + " will have " + mark)
print(Player2_name + " will have " + mark2)

# Asking for the start
asking_for_the_start()
# Game with Replay
game()
