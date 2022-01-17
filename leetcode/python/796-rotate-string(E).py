class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        length = len(s)
        
        for i in range(length):
            
            string = s[-1*i:] + s[:-1 * i]
            
            if string == goal:
                return True
        
        return False
        