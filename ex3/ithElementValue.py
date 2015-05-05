#####################################################################
# FILE: ithElementValue.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex3 2014-2015
# DESCRIPTION:
# This program prints the number in an Nth position in a Fibonnaci
# sequence. 

# "I do not love the bright sword for it's sharpness, nor the arrow
# for it's swiftness, nor the warrior for his glory. I love only that
# which they defend". 
#       - Tolkien
#####################################################################
orc_base = 1
orc_step = 1

orc_num= int(input("Which Orc do you wish to confront?"))

for i in range(2,orc_num):
    orc_step = orc_step + orc_base
    orc_base = orc_step - orc_base
    
print("The required number of arrows is", orc_step)
