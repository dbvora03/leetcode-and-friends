class RandomizedSet:

    def __init__(self):
        self.cache = set()
        

    def insert(self, val: int) -> bool:
        
        if val in self.cache:
            return False
        else:
            self.cache.add(val)
            return True        
        

    def remove(self, val: int) -> bool:
        
        if val in self.cache:
            self.cache.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        import random
        
        return random.sample(self.cache, 1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()