#####################################################################
# FILE: findSecondSmallest.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex3 2014-2015
# DESCRIPTION:
# This program recieves 10 ages and searches for the second smallest.
# The program will prints pippin's position.
#
# Home is behind, the world ahead,
# And there are many paths to tread
# Through shadows to the edge of night,
# Until the stars are all alight.
# Then world behind and home ahead,
# We'll wander back to home and bed...
#
#####################################################################
 
NUM_OF_DANCERS = 10             # as per definition


for i in range(NUM_OF_DANCERS):
    dancer_age = float(input("What is the age of the current dancer?"))

    # initialization for the smallest position
    if i == 0:          
        smallest_age = dancer_age
        smallest_pos = i
        continue    
        
    elif smallest_age > dancer_age:
        sec_smallest_age = smallest_age
        smallest_age = dancer_age
        pippin_pos = smallest_pos
        smallest_pos = i

    # initialize second smallest if it's the second input or check as normal
    # if it's smaller than sec_smallest because by now it's not smaller than
    # the smallest age
    elif i == 1 or sec_smallest_age > dancer_age: 
        sec_smallest_age = dancer_age
        pippin_pos = i
    
print("Pippin is dancer number",pippin_pos + 1)
