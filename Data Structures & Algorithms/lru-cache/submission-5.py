class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.cap = capacity
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        temp = self.right.prev
        self.right.prev.next = node
        node.prev = temp
        self.right.prev = node
        node.next = self.right
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            self.insert(self.hashMap[key])
            return self.hashMap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].val = value
            self.remove(self.hashMap[key])
            self.insert(self.hashMap[key])
        else:
            self.hashMap[key] = ListNode(key, value)
            self.insert(self.hashMap[key])
            if len(self.hashMap) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.hashMap[lru.key]

