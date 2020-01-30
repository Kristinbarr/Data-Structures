import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        save_root = self.value
        # if less, go left
        # print('COMPARE:', self.value, value)
        if value < self.value:
            print('LEFT: ',self.value, value)
            if self.left == None:
                self.left = BinarySearchTree(value)
                print('left val:', self.left)
                return
            else:
                # is something is there, go down a level
                self.left.insert(value)
        # if greater or same, go right
        else: # value >= self.value:
            print('RIGHT: ', self.value, value)
            if not self.right:
                self.right = BinarySearchTree(value)
                print('right val:', self.left)
                return
            else:
                # try again from child
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if value is root node
        # if less, go left
            # try again from child
        # if >= go right
            # try again from child
        # else no child, return None

        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until no more right
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
