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
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if key is in storage
        if key in self.storage:
            # move it to the start/head
            node = self.storage[key]
            print('GETTING! node:', node)
            self.order.move_to_front(node)
            # return the value
            return node.value[1]
            
        # if not in storage
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
    # storage-dict = { 
    #   key1: Node( value:(key1, val1), next:..., prev:... ),
    #   key2: Node( value:(key2, val2), next:..., prev:... ),
    #   key3: Node( value:(key3, val3), next:..., prev:... )
    # }

    def set(self, key, value):
        # create set first since get can't work without setting first
        # I chose most recent as head, oldest as tail

        # if key is found in dict,
        if key in self.storage:
            # overwrite existing value
            node = self.storage[key]
            node.value = (key, value)
            # move new node to head
            self.order.move_to_front(node)
            return

        # if cache is full,
        if self.size == self.limit:
            # delete the cur tail in dict/storage
            # self.order.tail.value is a tuple, [0] is the key
            # we save a tuple to get the key from the oldest node
            oldest_key = self.order.tail.value[0]
            del self.storage[oldest_key]
            # remove one from tail
            self.order.remove_from_tail()
            self.size -= 1
        
        # create new node and set it as new head
        self.order.add_to_head((key,value))
        # add new node to dict
        self.storage[key] = self.order.head
        self.size += 1

