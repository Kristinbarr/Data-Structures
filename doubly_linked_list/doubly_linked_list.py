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

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        # if self.head is none, tail is also none, set both to new node
        if not self.head and not self.tail:
            # empty list, this is head and tail
            self.head = new_node
            self.tail = new_node
        # update previous head
        # this needs to be current head bc we're adding to head
        else:
            # save self.head since it will be overwritten
            # new_node.next = self.head
            # self.head.prev = new_node
            # self.head = new_node

            # alternative solution using .insert_before
            self.head.insert_before(value)
            self.head = self.head.prev

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # save value of cur head to return
        value = self.head.value
        # node delete method will set the correct pointers
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        # if tail and head are none, set new_node to both
        if not self.head and not self.tail:
            # empty list, this is head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # we know that the list is populated
            self.tail.insert_after(value)
            self.tail = self.tail.next

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # save value of cur tail to return
        value = self.tail.value
        # node delete method will set the correct pointers
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # # # if the node is at the front, it is where it should be
        # if node is self.head:
        #     return
        # # save node value
        # value = node.value
        # # if the tail is the node, first step: remove from tail
        # if node is self.tail:
        #     self.remove_from_tail()
        # # else delete the node
        # else:
        #     node.delete()
        # # next add node to the head
        # self.add_to_head(value)

        # ALTERNATE VERSION
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # if LL i empty
        if not self.head and not self.tail:
            print('ERR: attempted to delete node not in list')
            return
        # if node is both head and tail, set pointers to None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        # if node is head
        elif node == self.head:
            # take node at next pointer, set it to cur head
            self.head = self.head.next
            node.delete()
        # if node is tail
        elif node == self.tail:
            # take node at prev pointer, set it to cur tail
            self.tail = self.tail.prev
            node.delete()
        # node is in middle
        else:
            node.delete()

        # update length
        self.length -= 1
    """Returns the highest value currently in the list"""
    def get_max(self):
        # if no head, there is no max value
        if self.head == None:
            print('ERROR: empty list')
            return
        else:
            # save current node and change to iterate
            cur_node = self.head
            # save max val, init as first val
            max_val = self.head.value
            while cur_node is not None:
                if cur_node.value > max_val:
                    max_val = cur_node.value
                # iterate by changing node to the next node
                cur_node = cur_node.next
            return max_val

