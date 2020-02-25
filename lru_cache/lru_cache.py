from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):

        # if key is in dict, move to tail bc its most recently used
        if key in self.storage:
            # save found node
            node = self.storage[key]
            # move to tail
            self.order.move_to_end(node)
            # access node's value and return it
            return node.value[1]
        #  if key not found, return none
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # for this case, HEAD is LEAST recently used, TAIL is MOST

        # if key found, update node, set as head of ll
        if key in self.storage:
            # create node 'shell' from key in dict, O(1)
            node = self.storage[key]
            # set value of node shell to tuple
            node.value = (key, value)
            # move to tail of LL
            self.order.move_to_end(node)
            return

        # if dict full, remove tail node from LL and dict
        if self.size == self.limit:
            # delete least recently used node (at head)
            # [0] is first value in tuple, it's used as key for dict
            del self.storage[self.order.head.value[0]]
            # move new node to head
            self.order.remove_from_head()
            # why do we subtract here?
            self.size -= 1

        # else key not found, add new node to tail of LL
        self.order.add_to_tail((key, value))
        # add key and node to dict
        self.storage[key] = self.order.tail
        # increment after operations are complete
        self.size += 1
