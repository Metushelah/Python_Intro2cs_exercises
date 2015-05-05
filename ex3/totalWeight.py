#####################################################################
# FILE: totalWeight.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex3 2014-2015
# DESCRIPTION:
# This program recieves weights until it either reaches 100 which
# is the maximum load a hobbit could carry, or the One Ring is
# inserted as a '-1' input.
# Don't forget the pipe !
#####################################################################
 
MAX_LOAD = 100
load = 0
weight = 0

print("Insert weights one by one:")

# checks and adds the loads to the bag
while load <= MAX_LOAD and weight != -1:
    weight = float(input())
    #if weight == -1:
    #    break
    if weight < 0 and weight != -1:
        print("Weights must be non-negative")
    else:
        load += weight
    
    
# decides what to print depending on the ending condition
if load > max_load:
    print("Overweight! Gandalf will not approve.")
else:
    print("The total packed weight is", load)
    
    
    
