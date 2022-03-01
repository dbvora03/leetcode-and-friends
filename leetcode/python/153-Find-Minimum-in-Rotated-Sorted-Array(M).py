class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        
        ans = nums[0]
        
        while left <= right:
            
            if nums[left] < nums[right]:
                ans = min(ans, nums[left])
                break
            
            middle = (left + right) // 2
            
            ans = min(ans, nums[middle])
            
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        
        return ans
                