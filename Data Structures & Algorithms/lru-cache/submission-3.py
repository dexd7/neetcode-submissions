class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev, self.next = None, None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {} #key:node pair
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    def insert(self, node):
        temp = self.right.prev
        temp.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = temp
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        self.remove(self.hashMap[key])
        self.insert(self.hashMap[key])
        return self.hashMap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
        newNode = Node(key,value)
        self.hashMap[key] = newNode
        self.insert(newNode)
        if len(self.hashMap)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.hashMap[lru.key]

