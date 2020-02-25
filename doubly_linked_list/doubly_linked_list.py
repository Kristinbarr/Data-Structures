"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    # here so you don't need to reference source code?
    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create a new instance of ListNode with args value, prev, next
        new_node = ListNode(value, None, None)
        # increment self length
        self.length += 1

        # if head and tail are null (if it's an empty list)
        if not self.head and not self.tail:
            # set head and tail to new node
            self.head = new_node
            self.tail = new_node
        else: # re-arrange pointers
            # set the new node's next to cur head
            new_node.next = self.head
            # set the cur head's prev to the new node (set it up to be 2nd)
            self.head.prev = new_node
            # set new head (make the switch)
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # save cur head's value
        value = self.head.value
        # remove the cur head
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # create a new instance of ListNode with args value, prev, next
        new_node = ListNode(value, None, None)
        # increment self length
        self.length += 1

        # if head and tail are null (if it's an empty list)
        if not self.head and not self.tail:
            # set head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            # new node's prev will be the last
            new_node.prev = self.tail
            # cur tail's next will be the new node
            self.tail.next = new_node
            # switch tail to be the new node
            self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # save cur tail's value
        value = self.tail.value
        # delete cur tail with delete method
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # save value of cur node
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # update length right away
        self.length -= 1

        # if LL is empty
        if not self.head and not self.tail:
            # TODO: error handling
            return

        # if the cur head and tail are same, make it and empty list
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # else if the node sent in is the head
        elif self.head == node:
            # set new head to cur head's next
            self.head = self.head.next
            node.delete()

        # else if the node sent in is the tail
        elif self.tail == node:
            # set new tail to cur tail's prev node
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        # if head doesn't exist, return none
        if not self.head:
            return None

        # variable for keep the highest value
        max_value = self.head.value
        # variable for the cur node's value
        current = self.head.next

        # traverse through list with while loop
        while current:
            # if cur val is greater, re-assign
            if current.value > max_value:
                max_value = current.value
        # new current value is the next value
            current = current.next
        return max_value
