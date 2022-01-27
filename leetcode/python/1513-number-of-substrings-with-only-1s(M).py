class Solution:
    def numSub(self, s: str) -> int:
        
        substrings = s.split('0')
        
        ans = 0
        
        for sub in substrings:
            
            ans += (len(sub) + 1) * len(sub) // 2
        
        return ans % ((10**9) + 7)
