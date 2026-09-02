class ListNode:
    def __init__(self, key, val):
        self.next = None
        self.val = val
        self.key = key
class MyHashMap:

    def __init__(self):
        self.hashSet = [ListNode(0, 0) for i in range(10**4)]


    def put(self, key: int, value: int) -> None:
        hash_location = key%len(self.hashSet)
        cur = self.hashSet[hash_location]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key: int) -> int:
        hash_location = key%len(self.hashSet)
        cur = self.hashSet[hash_location]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        hash_location = key%len(self.hashSet)
        cur = self.hashSet[hash_location]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)