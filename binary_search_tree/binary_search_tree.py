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
        # if self == None:
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
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass
        # call cb on self.value
        cb(self.value)
        # if left is present,
        if self.left:
            # call for_each
            self.left.for_each(cb)
        # if right is present,
        if self.right:
            # call for_each
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

#            (1)
#              (8)
#            (5)
#         (3)   (7)
#      (2) (4) (6)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # find smallest value
        if self.left:
            # recurse on left side
            self.left.in_order_print(self.left)
        # after no more left nodes and no more invocations,
        # print once past calling all left nodes
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create new queue
        queue = Queue()
        # add root to queue
        queue.enqueue(node)
        # while queue is not empty,
        while queue.size > 0:
            # save and remove cur head of queue
            temp = queue.dequeue()
            # print current node
            print(temp.value)
            # if temp has right,
            if temp.right:
                # add right node to queue
                queue.enqueue(temp.right)
            # if temp has left,
            if temp.left:
                # add left node to queue
                queue.enqueue(temp.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # push root to stack
        stack = Stack()
        stack.push(node)
        # while stack not empty
        while stack.size > 0:
            # pop top item out of stack into temp
            temp = stack.pop()
            print(temp.value)
            # if right,
            if temp.right:
                # put into stack
                stack.push(temp.right)
            # if left,
            if temp.left:
                # put into stack
                stack.push(temp.left)


    # STRETCH Goals -------------------------
    # Note: Research may be required
#         (1)
#           (8)
#         (5)
#      (3)   (7)
#   (2) (4) (6)

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        # print cur value immediately
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self.left)
        if self.right:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self.left)
        if self.right:
            self.right.post_order_dft(self.right)
        # print after all recursive calls have been evaluated
        print(self.value)

