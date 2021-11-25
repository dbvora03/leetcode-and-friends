class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        
        currentSum = 0
        for i, a in enumerate(nums):
            
            if currentSum + a > a:
                currentSum += a
            else:
                currentSum = a
            if currentSum > maxSum:
                maxSum = currentSum
            
        return maxSum