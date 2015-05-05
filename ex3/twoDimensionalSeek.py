#####################################################################
# FILE: twoDimensionalSeek.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex3 2014-2015
# DESCRIPTION:
# This program recieves the hobbits instructions with Left Right
# and number of steps taken, and prints the number of steps needed
# from the begining to reach the end in a two dimension.
#
# why couldn't they just take the ring on the back of an eagle?!
#####################################################################
x_coord = 0         # will hold gandalfs instructions in the end
y_coord = 0         # will hold gandalfs instructions in the end

look = 'up'         # will hold the reference to which direction we
                    #   are traveling on, up, right, left, down


""" In this part we address the issue of where the hobbits are facing
    and after each choice it updates the direction they are looking at.
    This direction also dictates the options they have for travel.
"""

while True:
    turn = input("Next turn:")
    if turn == "end":
        break
    else:
        steps = int(input("How many steps?"))
        
        if look == 'up':
            if turn == 'right':
                x_coord += steps
                look = 'right'
            else:
                x_coord -= steps
                look = 'left'
        
        elif look == 'right':
            if turn == 'right':
                y_coord -= steps
                look = 'down'
            else:
                y_coord += steps
                look = 'up'
        
        elif look == 'left':
            if turn == 'right':
                y_coord += steps
                look = 'up'
            else:
                y_coord -= steps
                look = 'down'
        
        elif look == 'down':
            if turn == 'right':
                x_coord -= steps
                look = 'left'
            else:
                x_coord += steps
                look = 'right'



""" This part calculates the instruction and prints the concated string
"""


instruction = "Gandalf should fly "

if x_coord < 0:
    instruction += str(-(x_coord)) + " steps left"
else:
    instruction += str(x_coord)+" steps right"

instruction += " and "

if y_coord < 0:
    instruction += str(-(y_coord))+" steps backward"
else:
    instruction += str(y_coord)+" steps forward"
    
print(instruction)
