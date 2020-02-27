import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # pushing adds to head
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        # pop removes from head
        if self.size == 0:
            return None
        else:
            self.size -= 1
            # need to return something
            return self.storage.remove_from_head()

    def len(self):
        return self.size
