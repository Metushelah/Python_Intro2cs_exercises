#!/usr/bin/env python3


class WordTracker(object):
    """
    This class is used to track occurrences of words.
     The class uses a fixed list of words as its dictionary
     (note - 'dictionary' in this context is just a name and does
     not refer to the pythonic concept of dictionaries).
     The class maintains the occurrences of words in its
     dictionary as to be able to report if all dictionary's words
     were encountered.
    """

    def __init__(self, word_list):
        """
        Initiates a new WordTracker instance.
        :param word_list: The instance's dictionary.
        """
        self.__word_list = self.__merge_sort(word_list)
        self.__encountered_word = [False] * len(word_list)

    
    def __contains__(self, word):
        """
        Check if the input word is contained within dictionary.
         For a dictionary with n entries, this method guarantees a
         worst-case running time of O(n) by implementing a
         binary-search.
        :param word: The word to be examined if contained in the
        dictionary.
        :return: True if word is contained in the dictionary,
        False otherwise.
        """
        result = self.__binary_search(word)
        if result != -1:
            return True
        return False


    # i am using the algorithm for Binary search presented in the
    # presentation given in the tirgul
    def __binary_search(self, word):
        """
        This is a helper function that does the binary search
        :param word: the word to search for
        :return: return the index of this word in the dictionary
        """
        left = 0
        right = len(self.__word_list) - 1
        idx = -1
        while (left <= right):
            middle_idx = (left + right) // 2
            middle = self.__word_list[middle_idx]
            if (middle == word):
                idx = middle_idx
                break
            elif (middle > word):
                right = middle_idx - 1
            else:
                left = middle_idx + 1
        return idx


    def encounter(self, word):
        """
        A "report" that the given word was encountered.
        The implementation changes the internal state of the object as
        to "remember" this encounter.
        :param word: The encountered word.
        :return: True if the given word is contained in the dictionary,
        False otherwise.
        """
        result = self.__binary_search(word)
        if result != -1:
            self.__encountered_word[result] = True
            return True
        return False


    def encountered_all(self):
        """
        Checks whether all the words in the dictionary were
        already "encountered".
        :return: True if for each word in the dictionary,
        the encounter function was called with this word;
        False otherwise.
        """
        for value in self.__encountered_word:
            if not value:
                return False
        return True


    def reset(self):
        """
        Changes the internal representation of the instance such
        that it "forget" all past encounters. One implication of
        such forgetfulness is that for encountered_all function
        to return True, all the dictionaries' entries should be
        called with the encounter function (regardless of whether
        they were previously encountered ot not).
        """
        for i in range(len(self.__encountered_word)):
            self.__encountered_word[i] = False


    # I will be using the same algorithm we had for merge sort in the
    # presentation shon in the tirgul
    def __merge_sort(self, lst):
        """
        This function takes in a list and using merge sort, sorts it
        :param lst: the lst to sort
        :return: a new sorted list
        """
        if len(lst) <= 1:
            return lst
        middle_val = len(lst)//2
        left_lst = self.__merge_sort(lst[:middle_val])
        right_lst = self.__merge_sort(lst[middle_val:])
        merged_lst = self.__merge(left_lst, right_lst)
        return merged_lst


    def __merge(self, left, right):
        """
        This is a helper function that merges two lists while sorting them
        :param left: left list
        :param right: right list
        :return: a new sorted list
        """
        new_lst = left + right
        l, r = 0, 0
        for i in range(len(left) + len(right)):
            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None
            if (lval and rval and lval < rval) or rval is None:
                new_lst[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                new_lst[i] = rval
                r += 1
        return new_lst


    def get_word_list(self):
        """
        This is a function for testing purposes
        :return: returns the word list sorted
        """
        return self.__word_list

