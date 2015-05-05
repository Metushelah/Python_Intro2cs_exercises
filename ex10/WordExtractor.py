#!/usr/bin/env python3


class WordExtractor(object):
    """
    This class should be used to iterate over words contained in files.
     The class should maintain space complexity of O(1); i.e, regardless
     of the size of the iterated file, the memory requirements ofa class
     instance should be bounded by some constant.
     To comply with the space requirement, the implementation may assume
     that all words and lines in the iterated file are bounded by some
     constant, so it is allowed to read words or lines from the
     iterated file (but not all of them at once).
    """
    EOF_SYMBOL = ''         #End of File symbol constant
    EOL_SYMBOL = '\n'       #End of Line symbol constant


    def __init__(self, filename):
        """
        Initiate a new WordExtractor instance whose *source file* is
        indicated by filename.
        :param filename: A string representing the path to the instance's
        *source file*
        """
        self.__filename = filename  # saves the file path
        self.__last_pos = 0         # initiates position of file to 0
        self.__words = []           # initiates word list to empty
        self.__word_index = 0       # initiates word count in list to 0


    def __iter__(self):
        """
        Returns an iterator which iterates over the words in the
        *source file* (i.e - self)
        :return: An iterator which iterates over the words in the
        *source file*
        """
        return self


    def __next__(self):
        """
        Make a single word iteration over the source file.
        The function reads a line each time it's list of words is done
        iterating over
        :return: A word from the file.
        """

        if self.__word_index >= len(self.__words):
            self.__word_index = 0
            with open(self.__filename, 'r') as file:
                file.seek(self.__last_pos)
                line = file.readline()

                while line == self.EOL_SYMBOL:
                    line = file.readline()
                if line == self.EOF_SYMBOL:
                    raise StopIteration
                else:
                    self.__words = line.split()
                    self.__last_pos = file.tell()

        self.__word_index += 1
        return self.__words[self.__word_index - 1]

