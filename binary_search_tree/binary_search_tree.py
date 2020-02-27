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

        # if there is no node at root: why does this work?
        # if self.value == None:
        #     print('self is NONE', self.value)
        #     # insert value as root
        #     self.value = BinarySearchTree(value)
        #     print('inserted val: ', self.value)

        # if value is smaller than root,
        if value < self.value:
            # if left node is present, 
            if self.left == None:
                # insert new 'tree' on left
                self.left = BinarySearchTree(value)
            else:
                # repeat steps on left side
                self.left.insert(value)
    
        # if value is greater or equal than root,
        else:
            # if right node is present,
            if self.right == None:
                # insert new 'tree' on right
                self.right = BinarySearchTree(value)
            else:
                # repeat steps on right side
                self.right.insert(value)

#         (5)
#     (2)    (7)
#      (3)
# target = 7

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target is equal to root:
        if target == self.value:
            return True
        
        # if no root node: why doesn't this work?
        # if self.value == None:
        #     print('NOT FOUND!')
        #     return False

        # if target is smaller than the root:
        if target < self.value:
            if self.left == None:
                return False
            # repeat on left
            return self.left.contains(target)

        # if target is larger than root:
        else: # target >= self.value:
            if self.left == None:
                return False
            # repeat on right side
            return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
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
