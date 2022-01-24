class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.data:
            value = self.data[key]
            del self.data[key]
            self.data[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.data:
            del self.data[key]
        
        elif len(self.data) == self.capacity:
            self.data.popitem(last = False)
        
        self.data[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)