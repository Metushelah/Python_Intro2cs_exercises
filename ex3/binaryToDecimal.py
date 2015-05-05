#####################################################################
# FILE: binaryToDecimal.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex3 2014-2015
# DESCRIPTION:
# This program recieves a binary number and transfers it into decimal
# representation.
#####################################################################

bin_to_convert = int(input("Insert number in binary representation:"))

decimal_sum = 0
BINARY_BASE = 2
multiplication_factor = 1

while True:
    binary_num = bin_to_convert % 10
    bin_to_convert //= 10
    
    decimal_sum += (binary_num * multiplication_factor)
    multiplication_factor *= BINARY_BASE
    
    if bin_to_convert == 0:
        break

print("The decimal value of the inserted binary number is", decimal_sum)

