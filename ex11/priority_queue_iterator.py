# FILE: priority_queue_iterator.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex11 2014-2015
# DESCRIPTION:
# This hold the class for iterating over our priority_queue

import node
import priority_queue

class PriorityQueueIterator:
    def __init__(self, queue):
        """
        This function initializes the iterator
        :param queue: a PriorityQueue type object
        :return: a PriorityQueueIterator type object
        """
        self.__queue = queue
        self.__curr = self.__queue.get_head()

    def __iter__(self):
        """
        This function creates and returns the iterator object
        :return: an iterator
        """
        return self

    def __next__(self):
        """
        This function returns the next task inside the Node in the order
        :return: task type
        """
        if self.has_next():
            temp = self.__curr
            self.__curr = self.__curr.get_next()
            return temp.get_task()
        else:
            raise StopIteration

    def has_next(self):
        """
        This function returns True or False if it has a next object to return
        :return: True of False
        """
        return self.__curr is not None
