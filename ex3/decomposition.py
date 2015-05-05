#####################################################################
# FILE: decomposition.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex3 2014-2015
# DESCRIPTION:
# This program recieves a number and breaks it up into its forming
# digits starting from the left.
#
# Gimli: It's true you don't see many dwarf women. And in fact, they
# are so alike in voice and appearance, that they are often mistaken
# for dwarf men.
# Aragorn:[whispering] It's the beards.
# Gimli: And this in turn has given rise to the belief that there are
# dwarf women, and that dwarves just spring out of holes in the ground!
# [Eowyn laughs]
# Gimli: Which is, of course, ridiculous.
#####################################################################

# the input to get the number to decompose 
number_to_decompose = int(input("Insert composed number:"))
day_num = 1
 

# this loops will check to see if there are numbers and check if any
# numbers are left to decompose after the last decomposition
# it will also print the results
while True:
    goblet_num = number_to_decompose % 10
    number_to_decompose //= 10
    
    print("The number of goblets Gimli drank on day", day_num,
                                                        "was", goblet_num)
    day_num += 1
    
    # here we check if any numbers are left after this last print
    # if the number equals 0 it means this was the last digit
    # to print. We will not address any 0's after the last digit.
    if number_to_decompose == 0:
        break
