#####################################################################
# FILE: findLargest.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex3 2014-2015
# DESCRIPTION:
# This program recieves number of items and returns the position
# of the Largest one.
# "A wizard is never late... nor is he early. He arrives precisely
# when he means to"    - Gandalf
#####################################################################
 
num_of_riders = int(input("Enter the number of riders:"))
gandalf_pos = -1
highest_hat = -1
 
for i in range(num_of_riders):
    hat_tall = int(input("How tall is the hat?"))
    if hat_tall > highest_hat:
        highest_hat = hat_tall
        gandalf_pos = i
    
print("Gandalf's position is:",gandalf_pos + 1)
