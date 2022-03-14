class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        
        def backtracking(path):
            if len(path) == 2*n:
                ans.append(path)
                return 
            
            opens = path.count("(")
            closes = path.count(")")
            if opens < n:
                backtracking(path + "(")
            
            if closes < opens:
                backtracking(path + ")")
        
        backtracking("")
        return ans
        