class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.val = 0

class MyHashMap:

    def __init__(self):
        self.hashMap = [ListNode(0) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        hash_func = key%(10**4)
        cur = self.hashMap[hash_func]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key)
        cur.next.val = value
        

    def get(self, key: int) -> int:
        hash_func = key%(10**4)
        cur = self.hashMap[hash_func]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        hash_func = key%(10**4)
        cur = self.hashMap[hash_func]
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