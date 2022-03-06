class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        answer = nums[0] + nums[1] + nums[2]
        
        nums.sort()
        
        
        for i in range(len(nums) - 2):
            
            if nums[i] == nums[i - 1] and i > 0:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                
                total = nums[i] + nums[left] + nums[right]

                
                if total == target:
                    return total
                
                if abs(total - target) < abs(answer - target):
                    answer = total                
                
                
                if total < target:
                    left += 1
                else:
                    right -= 1
                
        return answer