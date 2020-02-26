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
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        pass

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
        # create set first since get can't work without setting first

        # if key not found, create node and move key to head
        if not key in self.storage:
            self.cache.add_to_head(value)
            self.storage[key] = self.cache.head
            self.size += 1
        # if cache full, remove from tail, add new to head
        elif key in self.storage and self.cache.length == self.limit:
            print('\nnode?', self.storage[key].prev)
            # remove one from tail
            self.cache.remove_from_tail()
            # add new node to head
            self.cache.add_to_head(value)

        # if key found in dict, move node to head
        elif key in self.storage:
            self.cache.move_to_front(self.storage[key])

