class MyHashMap:

    def __init__(self):
        self.hashMap = []


    def put(self, key: int, value: int) -> None:
        if len(self.hashMap) == 0:
            self.hashMap.append([key,value])
        else:
            for i, pair in enumerate(self.hashMap):
                k= pair[0]
                if k == key:
                    self.hashMap[i][1] = value
                    return
            else:
                self.hashMap.append([key,value])


    def get(self, key: int) -> int:
        for pair in self.hashMap:
            k,v = pair
            if k == key:
                return v
        else:
            return -1
        

    def remove(self, key: int) -> None:
        for i,pair in enumerate(self.hashMap):
            k,v = pair
            if k == key:
                self.hashMap.pop(i)

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)