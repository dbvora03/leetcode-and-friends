class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        N = len(nums)
        ans = []
        nums.sort(reverse=True)
        vis = {}

        for i in range(0, N-2):
    
            l = i+1
            r = N-1
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                
                if sum == 0:
                    potential_ans = tuple([nums[i], nums[l], nums[r]])
                    if potential_ans not in vis:
                        vis[potential_ans] = 1
                        ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif sum > 0:
                    l += 1
                else:
                    r -= 1
            
        return ans