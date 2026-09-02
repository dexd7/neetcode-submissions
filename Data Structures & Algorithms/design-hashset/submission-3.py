class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val
class MyHashSet:

    def __init__(self):
        self.hashSet = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        hash_location = key%len(self.hashSet)
        cur = self.hashSet[hash_location]
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
            

    def remove(self, key: int) -> None:
        hash_location = key%len(self.hashSet)
        cur = self.hashSet[hash_location]
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        
            

    def contains(self, key: int) -> bool:
        hash_location = key%len(self.hashSet)
        cur = self.hashSet[hash_location]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)