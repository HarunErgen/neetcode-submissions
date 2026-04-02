class Node:
    def __init__(self, val: int, key: int = None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashset = dict()
        self.dummy = Node(float("-inf"))
        self.tail = None

    def get(self, key: int) -> int:
        node = self.hashset.get(key)
        if node is None:
            return -1
        self.promote(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        node = None
        if key not in self.hashset:
            node = Node(value, key)
            self.hashset[key] = node
            node.next, node.prev = self.dummy.next, self.dummy
            if self.dummy.next:
                self.dummy.next.prev = node
            self.dummy.next = node
            if self.tail is None:
                self.tail = node
            if len(self.hashset) > self.capacity:
                self.remove_last()
        else:
            node = self.hashset.get(key)
            node.val = value
            self.promote(node)

    def promote(self, node: Node):
        if self.dummy.next == node: return
        if self.tail == node:
            self.tail = node.prev

        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        self.dummy.next.prev = node
        node.next, node.prev = self.dummy.next, self.dummy
        self.dummy.next = node

    def remove_last(self):
        del self.hashset[self.tail.key]
        prev = self.tail.prev
        prev.next = None
        self.tail = prev
