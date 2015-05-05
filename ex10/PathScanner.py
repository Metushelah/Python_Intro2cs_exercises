import os
import WordTracker as Track
import WordExtractor as Extract


class PathIterator:
    """
    An iterator which iterates over all the directories and files
    in a given path (note - in the path only, not in the
    full depth). There is no importance to the order of iteration.
    """
    def __init__(self, path):
        """
        This functions initializes an iterator object
        """
        self.__path = path
        self.__content = os.listdir(self.__path)
        self.__current = 0


    def __iter__(self):
        """
        this function returns an iter object
        """
        return self


    def __next__(self):
        """
        this function returns the next item in the list of content
        """
        if self.__current == len(self.__content):
            raise StopIteration
        else:
            self.__current += 1
            return os.path.join(self.__path, self.__content[self.__current-1])


def path_iterator(path):
    """
    Returns an iterator to the current path's files and directories.
    Note - the iterator class is not outlined in the original
     version of this file - but rather is should be designed
     and implemented by you.
    :param path: A (relative or an absolute) path to a directory.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :return: An iterator which returns all the files and directories
    in the *current* path (but not in the *full depth* of the path).
    """
    return PathIterator(path)


def print_tree(path, sep='  '):
    """
    Print the full hierarchical tree of the given path.
    Recursively print the full depth of the given path such that
    only the files and directory names should be printed (and not
    their full path), each in its own line preceded by a number
    of separators (indicated by the sep parameter) that correlates
    to the hierarchical depth relative to the given path parameter.
    :param path: A (relative or an absolute) path to a directory.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :param sep: A string separator which indicates the depth of
     current hierarchy.
    """
    def print_tree_helper(path, cur_sep, sep_to_add):
        tree = path_iterator(path)
        for branch in tree:
            split = os.path.split(branch)
            print (cur_sep + split[1])
            if os.path.isdir(branch):
                print_tree_helper(branch, cur_sep + sep_to_add, sep_to_add)

    print_tree_helper(path, "" , sep)


def file_with_all_words(path, word_list):
    """
    Find a file in the full depth of the given path which contains
    all the words in word_list.
    Recursively go over  the files in the full depth of the given
    path. For each, check whether it contains all the words in
     word_list and if so return it.
    :param path: A (relative or an absolute) path to a directory.
    In the full path of this directory the search should take place.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :param word_list: A list of words (of strings). The search is for
    a file which contains this list of words.
    :return: The path to a single file which contains all the
    words in word_list if such exists, and None otherwise.
    If there exists more than one file which contains all the
    words in word_list in the full depth of the given path, just one
    of theses should be returned (does not matter which).
    """
    result = None
    tree = path_iterator(path)
    for branch in tree:
        if os.path.isfile(branch):
            extract = Extract.WordExtractor(branch)
            track = Track.WordTracker(word_list)
            for word in extract:
                track.encounter(word)
            if track.encountered_all():
                result = branch
        elif result == None and os.path.isdir(branch):
            result = file_with_all_words(branch, word_list)

    return result
    
    
