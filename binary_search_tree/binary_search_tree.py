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
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else: # if something is there, try again from child
                self.left.insert(value)

        # if greater or same, go right
        else: # value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                # if something is there, try again from child
                self.right.insert(value)

    # Return True if the tree contains the value
    # Return False if not
    def contains(self, target):
        # if value is root node
        if self.value == target:
            return True
        # if less, go left
        if target < self.value:
            # if the left node does exist, it's not in tree
            if not self.left:
                return False
            else:
                # try again from child
                # we return bc we need to 'report' what search finds
                return self.left.contains(target)
        else: # if >= go right
            # else no child, it's not in the tree, return False
            if not self.right:
                return False
            # try again from child
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # recursive solution: go right until no more right
        # if not self.right:
        #     return self.value
        # else:
        #     return self.right.get_max()

        # Iterative solution w while loop:
        max_value = self.value
        # create a reference to cur node and update it while traverse
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
            print('self val:', self.value)

        return max_value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call the same function on every node
        cb(self.value)
        print('FE enter: ', self.value)
        # if left is there, recurse and send the same cb function
        if self.left:
            print('FE left: ', self.left.value)
            self.left.for_each(cb)
        # if right is there, recurse and send the same cb function
        if self.right:
            print('FE right: ', self.right.value)
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if cur node has value (we're not at the leaf, keep going)
        if node:
            # recurse left until no node, we found smallest value
            self.in_order_print(node.left)
            # once finding smallest node unwinds, print smallest
            print(node.value)
            # then traverse right side of cur node
            self.in_order_print(node.right)


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
