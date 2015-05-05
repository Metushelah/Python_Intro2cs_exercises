#########################################################################
# FILE: nim.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex4 2014-2015
# DESCRIPTION:
# A small program which plays nim with the player or allows the player
# to play against another player.
#########################################################################
from computer_functions import get_computer_move, HEAPS


def print_heaps(heap_lst):
    """
    prints the heap list in graphical format
    :param: heap_lst
    :return: None
    """
    for i in enumerate(heap_lst):
        print(str(i[0]+1) + ":")
        str_2_print = "* " * i[1]
        print(str_2_print[:-1])


def check_row(row, heap_lst):
    """
    this checks if the row is correct 
    :param: row, heap_lst
    :return: True or False
    """
    if row < 1:
        return False
    elif row > len(heap_lst):
        return False
    elif heap_lst[row - 1] == 0:
        print("That row is empty")
        return False
    return True
        

def check_matches(matches, row, heap_lst):
    """
    this program checks if the number of matches specified is correct
    and according to what is inside the heaps
    :param: matches, row, heap_lst
    :return: True or False
    """
    if matches < 1:
        return False
    elif matches > heap_lst[row-1]:
        return False
    return True


def get_player_move(player_name, heap_lst):
    """
    Gets the player move and checks if it's a legal move.
    It returns the new move in the same format as the computer move
    :param: heap_lst
    :return: list with 2 parameters [i,j] , i for row and j for number
    """
    PLAYER_TURN_PRINT_SUFFIX = ", it's your turn:"
    row = -1
    matches = -1
    done = False

    print(player_name + PLAYER_TURN_PRINT_SUFFIX)

    while not done:
        row = int(input("Row?"))
        done = check_row(row, heap_lst)
    
    done = False    
    while not done:
        matches = int(input("How many?"))
        done = check_matches(matches, row, heap_lst)

    return [row - 1, matches]


def check_game_end(heap_lst):
    """
    if all the heaps are empty than the game ends
    :param: heap_lst
    :return: True if empty, False otherwise
    """
    if max(heap_lst) == 0:
        return True
    return False


def update_heaps(heap_lst, move):
    """
    this functions gets the heap_lst and updates according to move
    :param: heap_lst, move
    :return: the new updated heap_lst
    """
    heap_lst[move[0]] -= move[1]
    return heap_lst


def print_winner(player1_win):
    """
    this function gets the last turn who was the winner
    and prints his name from the names in the main.
    :param: player1_win
    :return: None
    """
    if num_players > 1:
        if player1_win:
            print(player1_name, "wins")
        else:
            print(player2_name, "wins")
    elif player1_win:
        print ("You win")
    else:
        print("Computer wins")


def game_play(player1turn):
    """
    this function plays the game according to the last turn given to it
    and continues until the board is clear
    :param: player1turn
    :return: player1turn
    """
    end_game = False
    heaps = list(HEAPS)
    print_heaps(heaps)

    while (not(end_game)):
        player1turn = not(player1turn)
        if player1turn == True:
            move = get_player_move(player1_name,heaps)
        else:
            if num_players > 1:
                move = get_player_move(player2_name,heaps)
            else:
                move = get_computer_move(heaps)
                print("Computer takes",move[1], "from row", move[0]+1)

        heaps = update_heaps(heaps,move)
        
        print_heaps(heaps)

        end_game = check_game_end(heaps)
        
        
    return player1turn

"""
This is the main function and it recieves the player names and how many
players there are, and runs the game as long as a 'Y' or 'y' is given
at the end of every game cycle
:param: None
:return: None
"""
#constants
MAX_NUM_OF_PLAYERS = 2
PLAY_AGAIN_TERMS = ['Y','y']

#variable init
player1turn = True
play_again = 'Y'

#this part initializes the game with number of players and their names
num_players = int(input("Please enter the number of human players (1 or 2):"))

if num_players != MAX_NUM_OF_PLAYERS:
    player1_name = input("Please enter your name:")
else:
    player1_name = input("Name of first player:")
    player2_name = input("Name of second player:")

# this is the play while 'Y' or 'y' is given and runs the game until
# specified otherwise
while play_again in PLAY_AGAIN_TERMS:
    player1turn = game_play(not(player1turn))
    print_winner(player1turn)
    play_again = input("Play again? (Y/N)")
