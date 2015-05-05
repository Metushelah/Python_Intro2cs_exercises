#####################################################################
# FILE: decimalToBinary.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex3 2014-2015
# DESCRIPTION:
# This program recieves a decimal number and transfers it into binary
# representation.
#####################################################################

dec_to_convert = int(input("Insert number in decimal representation:"))

binary_num = ""
BASE = 2

while True:
    remainder = dec_to_convert % BASE
    dec_to_convert //= BASE
    
    binary_num = str(remainder) + binary_num
    
    if dec_to_convert == 0:
        break

print("The binary value of the inserted decimal number is", binary_num)

