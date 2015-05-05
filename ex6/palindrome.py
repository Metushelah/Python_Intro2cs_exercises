#########################################################
# FILE: palindrome.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex6 2014-2015
# DESCRIPTION:
# This function hold two palindrome functions.
# palindrome1 checks if the whole string is palindrome.
# palindrome2 checks if the string between the indexes
# is a palindrome.
#
# "Do geese see God?"
#########################################################


def is_palindrome_1(s):
    """
    receives a string s and checks recursively if it's a palindrome
    :param s: the string to check
    :return: True of False for the palindrome
    """
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return True and is_palindrome_1(s[1:-1])
    else:
        return False


def is_palindrome_2(s, i, j):
    """
    receives a string s and checks if the the substring between i and j
    is a palindrome without using substring (s[i:j]).
    solves it recursively
    :param s: string containing the part to check between i and j
    :param i: index of lower bound
    :param j: index of higher bound
    :return: True of False if the substring is a palindrome
    """

    if i > j + 1:
        return False
    elif len(s) <= 1 or i-j == 0 or i == j+1:
        return True
    elif s[i] == s[j]:
        return True and is_palindrome_2(s, i+1, j-1)
    else:
        return False
