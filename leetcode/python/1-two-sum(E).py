class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        
        for i, a in enumerate(nums):
            potentialNumber = target - a
            
            if potentialNumber in cache:
                return [cache[potentialNumber], i]
            else:
                cache[a] = i