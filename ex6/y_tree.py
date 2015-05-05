########################################################################
# FILE: y_tree.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex6 2014-2015
# DESCRIPTION:
# Draws a tree using Turtle module recursively where each branch is 0.6
# the length of the previous one (in pixels) and the angle between branches
# is 60 degrees.
#
# "Of all the trees we could have hit, we had to get one that hits back "
#           - Ron, Harry Potter and the Chamber of Secrets
########################################################################
import turtle


def y_tree(length = 200):
    """
    This function receives a length and draws a tree according to the length
    in an angle 60 between the branches always reducing the next length by
    0.6. The drawing ends when the length is smaller than 10
    :param length: The length of the branch to draw, default 200
    :return: None
    """
    ANGLE_BETWEEN_BRANCHES = 60
    LENGTH_REDUCTION = 0.6
    MIN_LENGTH = 10


    if length <= MIN_LENGTH:
        return
    else:
        turtle.forward(length)                  # draws the branch
        turtle.left(ANGLE_BETWEEN_BRANCHES / 2)
        y_tree(LENGTH_REDUCTION * length)       # draws the left branch

        turtle.right(ANGLE_BETWEEN_BRANCHES)
        y_tree(LENGTH_REDUCTION * length)       # draws the right branch

        turtle.left(ANGLE_BETWEEN_BRANCHES / 2)
        turtle.backward(length)                 # returns back to draw next
