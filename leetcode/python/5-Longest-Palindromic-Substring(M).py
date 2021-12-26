class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLen = 0
        
        for i in range(len(s)):
            #check odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLen:
                    result = s[l:r+1]
                    resultLen = r - l + 1
                l -= 1
                r += 1
            
            #check even length
            l, r = i, i+1
            
            while l >= 0 and r <len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLen:
                    resultLen = r - l + 1
                    result = s[l:r+1]
                l -= 1
                r += 1
                
        return result