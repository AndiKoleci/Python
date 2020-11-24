from time import sleep
from random import randint


# The win_condition function checks if any of the 8 win possibilities happen.

def win_condition():
    if ValueList[1] == ValueList[2] and ValueList[2] == ValueList[3] and ValueList[1] == 'X':
        return 1
    elif ValueList[1] == ValueList[4] and ValueList[4] == ValueList[7] and ValueList[1] == 'X':
        return 1
    elif ValueList[1] == ValueList[5] and ValueList[5] == ValueList[9] and ValueList[1] == 'X':
        return 1
    elif ValueList[2] == ValueList[5] and ValueList[5] == ValueList[8] and ValueList[2] == 'X':
        return 1
    elif ValueList[3] == ValueList[6] and ValueList[6] == ValueList[9] and ValueList[3] == 'X':
        return 1
    elif ValueList[4] == ValueList[5] and ValueList[5] == ValueList[6] and ValueList[4] == 'X':
        return 1
    elif ValueList[7] == ValueList[8] and ValueList[8] == ValueList[9] and ValueList[7] == 'X':
        return 1
    elif ValueList[3] == ValueList[5] and ValueList[5] == ValueList[7] and ValueList[3] == 'X':
        return 1
    else:
        return 0


# The lose_condition function checks if any of the 8 win possibilities happen for the PC.

def lose_condition():
    if ValueList[1] == ValueList[2] and ValueList[2] == ValueList[3] and ValueList[1] == 'O':
        return 1
    elif ValueList[1] == ValueList[4] and ValueList[4] == ValueList[7] and ValueList[1] == 'O':
        return 1
    elif ValueList[1] == ValueList[5] and ValueList[5] == ValueList[9] and ValueList[1] == 'O':
        return 1
    elif ValueList[2] == ValueList[5] and ValueList[5] == ValueList[8] and ValueList[2] == 'O':
        return 1
    elif ValueList[3] == ValueList[6] and ValueList[6] == ValueList[9] and ValueList[3] == 'O':
        return 1
    elif ValueList[4] == ValueList[5] and ValueList[5] == ValueList[6] and ValueList[4] == 'O':
        return 1
    elif ValueList[7] == ValueList[8] and ValueList[8] == ValueList[9] and ValueList[7] == 'O':
        return 1
    elif ValueList[3] == ValueList[5] and ValueList[5] == ValueList[7] and ValueList[3] == 'O':
        return 1
    else:
        return 0


# This function processes the turn of the player and the turn of the PC, printing the board in the end.

def player_turn():
    while True:
        player_choice = int(input("Where do you want to put X?"))
        if ValueList[player_choice] == ' ':
            ValueList[player_choice] = 'X'
            break
        else:
            print("Pick another place please.")
            sleep(1)

    if win_condition() == 1:
        return 0

    while True:
        pc_choice = randint(1, 9)
        if ValueList[pc_choice] == ' ':
            ValueList[pc_choice] = 'O'
            break
    sleep(1)
    print_table()


# A simple function that prints the board.

def print_table():
    for value in range(1, 10):
        if value % 3 != 0:
            print("{} | ".format(ValueList[value]), end='')
        else:
            print("{}".format(ValueList[value]))


# This is a setup for the game, where i initialise the board and print it for the first time.


ValueList = []
for i in range(1, 11):
    ValueList.append(' ')
print_table()

# This is where the game starts. The game will end when one of the conditions is fulfilled.


while lose_condition() == 0 and win_condition() == 0:
    player_turn()
    if lose_condition() == 1:
        print("You lost!!")
        break
    elif win_condition() == 1:
        print("You won!!!!")
        print_table()
        break
