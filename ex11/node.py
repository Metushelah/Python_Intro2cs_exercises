# FILE: node.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex11 2014-2015
# DESCRIPTION:
# This module holds the Node class for the queue


class Node:
    def __init__(self, task, next_node = None):
        """
        Initializes our object instance
        :param task: The task the node object need to save
        :param next_node: The pointing to the next Node in the queue
        :return: a Node object
        """
        self.__task = task
        self.__next = next_node

    def get_priority(self):
        """
        This function returns the priority of the task at hand
        :return: priority level
        """
        return self.__task.get_priority()

    def set_priority(self, new_priority):
        """
        This function sets a new priority to the task
        :param new_priority: the new priority to set
        :return: None
        """
        self.__task.set_priority(new_priority)

    def get_task(self):
        """
        This function returns the current task the Node holds
        :return: the task inside the Node
        """
        return self.__task

    def get_next(self):
        """
        This function returns the next object in the queue
        :return: The pointer to the next object in the queue
        """
        return self.__next

    def set_next(self, next_node):
        """
        This function changes the Node we are pointing to next_node
        :param next_node: The new Node to point to
        :return: None
        """
        self.__next = next_node

    def has_next(self):
        """
        This function returns True of False whether we have a Node to point to
        :return: True of False according to next_node
        """
        return self.__next is not None