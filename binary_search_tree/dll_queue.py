import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # make a new node with value
        # reassign cur tail's next to new node
        self.storage.add_to_tail(value)
        # increment size
        self.size += 1

    def dequeue(self):
        # need to check if LL has any nodes
        if self.size == 0:
            return None
        else:
            # decrement size
            self.size -= 1
            # use remove from head method
            return self.storage.remove_from_head()


    def len(self):
        return self.size
