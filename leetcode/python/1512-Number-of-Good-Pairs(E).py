class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        cache = {}
        for i in range(len(nums)):
            if nums[i] not in cache:
                cache[nums[i]] = 1
            else:
                ans += cache[nums[i]]
                cache[nums[i]] += 1
        
        return ans