class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
          
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]: # LHS is sorted
                
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else: # RHS is sorted
                if nums[mid] < target and target <= nums[right]:
                    low = mid + 1
                else:
                    right = mid - 1
        return -1
                
        
                
        

        