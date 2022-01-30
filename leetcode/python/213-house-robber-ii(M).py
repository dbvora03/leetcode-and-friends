class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 3:
            return max(nums)
            
        return max(self.hr1(nums[1:]), self.hr1(nums[:-1]))
        
    def hr1(self, nums):
        rob1,rob2 = 0,0
        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2