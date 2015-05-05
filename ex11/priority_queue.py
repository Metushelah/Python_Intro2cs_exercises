# FILE: priority_queue.py
# WRITER : konstantin, guybrush, 30888377
# EXERCISE : intro2cs ex11 2014-2015
# DESCRIPTION:
# This holds the queue for our program
import node
import string_task
import priority_queue_iterator

class PriorityQueue:
    def __init__(self, tasks = []):
        """
        This function initializes our task queue
        :param tasks: the tasks we want to add to the queue if any
        :return: a PriorityQueue object
        """
        self.__head = None
        self.__curr = None
        self.__iter_curr = None    # will hold a different current marker as
                                   # not to be overridden in the other methods
        self.__size = 0
        temp_lst = sorted(tasks, key = lambda task : task.get_priority())
        for task in temp_lst:
            self.enque(task)

    def enque(self, task):
        """
        This function adds a new task to the queue
        :param task: the task to add
        :return: None
        """
        new_node = node.Node(task)

        # if queue is empty enter task in first place
        if self.__head is None:
            self.__head = new_node

        # if task is higher priority put it in first place
        elif self.__head.get_priority() < task.get_priority():
            new_node.set_next(self.__head)
            self.__head = new_node

        # else, search where the next is of less priority or None and put task
        else:
            self.__curr = self.__head
            while (self.__curr.get_next() is not None and
                            self.__curr.get_next().get_priority() >=
                                                        task.get_priority()):

                self.__curr = self.__curr.get_next()

            new_node.set_next(self.__curr.get_next())
            self.__curr.set_next(new_node)
        self.__size += 1

    def peek(self):
        """
        This function shows the first item in our queue
        :return: the task, a string object
        """
        if self.__head is None:
            return None
        return self.__head.get_task()

    def deque(self):
        """
        This function returns and removes the first item in the queue order
        :return: first task in queue, a Node object
        """
        if self.__head is not None:
            temp_addr = self.__head
            self.__head = self.__head.get_next()
            self.__size -= 1
            return temp_addr.get_task()

        else:
            return self.__head

    def get_head(self):
        """
        This function returns the head of the queue
        :return: returns a Node type object
        """
        return self.__head

    def change_priority(self, old, new):
        """
        This function searches for a task with the given old priority and if
        found changes it's priority to new and updates the queue
        :param old: the old priority to look for and change
        :param new: the new priority to put instead of the old one
        :return: None
        """
        # if queue is empty return None because there is no task to update
        if self.__head is None:
            return None
        # else if the head is of the same priority than update it
        elif self.__head.get_priority() == old:
            task = self.deque().get_task()  # get task out of Node we take out
            task.set_priority(new)
            self.enque(task)
            return None

        # else, search for the current task whos next task equals old,
        # will stop in the position of one before the task to update or the
        # last position in the queue before the None if not found any task
        self.__curr = self.__head
        while self.__curr.get_next() is not None and \
                            self.__curr.get_next().get_priority() != old:
            self.__curr = self.__curr.get_next()

        # this will happen if he found a task where the next task is of
        # priority equal to old, then it removes it, updates it and inserts
        # it back using enque()
        if self.__curr.get_next() is not None:
            task = self.__curr.get_next().get_task()
            self.__curr.set_next(self.__curr.get_next().get_next())
            task.set_priority(new)
            self.enque(task)
            self.__size -= 1  # we update size manualy because enque add 1 to
                              # size but we didn't really take any out

        # if reached here then there are no tasks with the old priority
        else:
            return None

    def __len__(self):
        """
        This function returns the size of our queue
        :return: an integer representing queue size
        """
        return self.__size

    def __iter__(self):
        """
        This function inits the iteration function
        :return: returns an iterable object
        """
        self.__iter_curr = self.__head  # for the __next__ function
        return priority_queue_iterator.PriorityQueueIterator(self)

    def __next__(self):
        """
        This function will return the next task at hand each time called
        :return: The task inside the next node in the queue
        """
        if self.__iter_curr is None:
            raise StopIteration
        else:
            temp = self.__iter_curr
            self.__iter_curr = self.__iter_curr.get_next()
            return temp.get_task()

    def __str__(self):
        """
        This function returns a string containing the whole queue in string
        :return: a string representing queue
        """
        # Constants when representing the string
        CONSTANTS_LST = ["[",", ","]"]

        self.__curr = self.__head
        result = ""
        while self.__curr is not None:
            result = result + repr(self.__curr.get_task())
            if self.__curr.get_next() is not None:
                result = result + CONSTANTS_LST[1]
            self.__curr = self.__curr.get_next()
        return CONSTANTS_LST[0] + result + CONSTANTS_LST[2]

    def __add__(self, other):
        """
        This function adds the content of another PriorityQueue into this one
        :param other: another PriorityQueue object
        :return: and updated PriorityQueue with the tasks of other in it
        """
        new_queue = PriorityQueue()
        for task in self:
            new_queue.enque(task)
        for task in other:
            new_queue.enque(task)
        return new_queue

    def __eq__(self, other):
        """
        This function compares each item in the two queues and returns True or
        False if they are the same or not
        :param other: the other PriorityQueue object to compare to
        :return: True or False if equal or not
        """
        # if they are not the same size than they are not equal
        if self.__size != len(other):
            return False

        self.__curr = self.__head
        other__curr = other.get_head()
        while self.__curr is not None:
            if self.__curr.get_task() != other__curr.get_task():
                return False
            self.__curr = self.__curr.get_next()
            other__curr = other__curr.get_next()
        return True
      
