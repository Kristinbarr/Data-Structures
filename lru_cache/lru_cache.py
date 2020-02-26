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
    #   key1: Node(value: (key1, val1) next:..., prev:...),
    #   key2: (key2, val2),
    #   key3: (key3, val3)
    # }

    def set(self, key, value):
        # create set first since get can't work without setting first

        print('SET! size:', self.size)

        # if key found in dict,
        if key in self.storage:
            # overwrite value
            node = self.storage[key]
            node.value = (key, value)
            # move node to head
            self.order.move_to_front(node)
            return

        # if cache is full,
        if self.size == self.limit:
            # delete the cur tail in dict/storage
            # self.order.tail.value is a tuple, [0] is the key
            cur_tail_key = self.order.tail.value[0]
            del self.storage[cur_tail_key]
            # remove one from tail
            self.order.remove_from_tail()
            # decrement size
            self.size -= 1
        
        # create new node and set it as new head
        # ?: why do we keep the value as a tuple?
        self.order.add_to_head((key,value))
        # add new node to dict
        self.storage[key] = self.order.head
        # increment size
        self.size += 1





# BRIANS HELP
    # # if cache is NOT empty(at least 1, maybe full):
    #     # if key is in dict, overwrite with new value
    #     if key in self.storage:
    #         node = self.storage[key]
    #         # overwrite val( put tuple as node's val)
    #         node.value = (key, value)
    #         # move it to end/head
    #         self.order.move_to_end(node)
    #         return
    #     # if cache is full
    #     if self.size == self.limit:
    #         # remove oldest from dict
    #         del self.storage[self.order.head.value[0]]
    #         # remove from LL
    #         self.order.remove_from_head()
    #         # decrement size
    #         self.size -= 1

    # # if cache is empty do all the below:
    #     # add to LL (key and val)
    #     self.order.add_to_tail((key, value))
    #     # add key and val to dict
    #     self.storage[key] = self.order.tail
    #     # increment size
    #     self.size += 1
