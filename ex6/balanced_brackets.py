#############################################################################
# FILE: balanced_brackets.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex6 2014-2015
# DESCRIPTION:
# ------------------------
# ---------------------


# "Life is like riding a bicycle, To keep your Balance, you must keep moving"
#############################################################################
def _is_balanced_help(s):
    """
    receives a string and checks the difference between the brackets
    :param s: string to check
    :return: -1 if more closing brackets than opening ones, or the difference
    between the brackets
    """
    LEFT_CHAR = "("
    RIGHT_CHAR = ")"
    left_count = 0
    right_count = 0
    for i in s:
        if i == LEFT_CHAR:
            left_count += 1
        elif i == RIGHT_CHAR:
            right_count += 1
        
        if right_count > left_count:
            return -1

    return left_count - right_count


def is_balanced(s):
    """
    receives a string and checks if it is balanced according to the number
    of brackets in them and it they keep the right order
    :param s: string to check
    :return: True if balanced False otherwise
    """
    result = _is_balanced_help(s)
    if result == 0:
        return True
    return False


def _violated_balanced_help(s):
    """
    This function checks recursively if the string given is balanced, if not
    it searches for the biggest string inside that is balanced
    :param s: the string to check
    :return: len of the biggest string that is balanced inside the first
    string
    """
    if is_balanced(s):
        return len(s)
    else:
        return _violated_balanced_help(s[:-1])
        


def violated_balanced(s):
    """
    This function checks where is there a problem (if any) in a string in
    regard to it's brackets. If there are more opening than closing it will
    return the length of the string otherwise it will return -1 if they are
    balanced or the first instance where they are not balanced.
    Checks recursively
    :param s: the string to check
    :return: -1 or the index to fix
    """
    BALANCED_RETURN = -1
    
    if is_balanced(s):
        return BALANCED_RETURN
    elif _is_balanced_help(s) > 0:
        return len(s)
    else:
        return _violated_balanced_help(s)
        


def match_brackets(s):
    """
    For a balanced string returns a list with the numbers signifying how much
    you need to move to reach the its partner bracket or 0 for not bracket
    chars. Returns an empty string for unbalanced strings.
    :param s: a string to check
    :return: empty list for unbalanced strings or a list
    """
    LEFT_CHAR = "("
    RIGHT_CHAR = ")"
    if not is_balanced(s):
        return []
    else:
        lst = [0] * len(s)
        for i in range(len(s)):
            if s[i] != LEFT_CHAR and s[i] != RIGHT_CHAR:
                lst[i] = 0 
            elif s[i] == LEFT_CHAR:
                difference = violated_balanced(s[i+1:]) + 1
                lst[i] = difference
                lst[i+difference] = -1 * difference
            
    return lst
