class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} #key-value pair of key-Node

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        """
        :type capacity: int
        """
    def remove(self, node):
        prv = node.prev
        nxt = node.next

        prv.next, nxt.prev = nxt, prv

    def insert(self, node):
        prevOfRight = self.right.prev
        prevOfRight.next = node
        self.right.prev = node

        node.prev = prevOfRight
        node.next = self.right

    def get(self, key):
        if key in self.cache:
            # TODO: update the MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
