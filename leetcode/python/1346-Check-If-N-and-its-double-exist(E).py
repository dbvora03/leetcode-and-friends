class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        cache = set()
        
        for number in arr:
            
            if number * 2 in cache or number / 2 in cache:
                return True
            else:
                cache.add(number)
        
        return False