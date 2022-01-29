class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        ans = ''
        
        space_index = 0
        for i in range(len(s)):
            if space_index < len(spaces):  
                if spaces[space_index] == i:
                    ans += ' '
                    space_index += 1
            
            ans += s[i]
        
        
        return ans