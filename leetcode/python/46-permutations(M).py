class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
    
        def dfs(ans):   
            if len(ans) == len(nums):
                res.append(ans.copy())
                return
            
            for number in nums:
                if number not in ans:
                    ans.append(number)
                    dfs(ans)
                    ans.pop()
        
        dfs([])
        return res