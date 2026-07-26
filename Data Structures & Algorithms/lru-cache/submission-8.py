class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:      
        node = self.cache.get(key)
        if node:
            self.remove(node)
            self.insert_at_end(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:

        node = self.cache.get(key)
        # update
        if node:
            self.remove(node)
            node.value = value
            self.insert_at_end(node)
        else:
            # insert
            new_node = Node(key, value)
            self.insert_at_end(new_node)

            if len(self.cache) > self.capacity:
                # remove
                least_used = self.head.next
                self.remove(least_used)
                self.cache.pop(least_used.key)
                
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
      
    def insert_at_end(self, node):
        self.cache[node.key] = node
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node
