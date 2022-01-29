class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        res = []
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        def rec(loc, answer):
            
            if len(answer) == len(digits):
                res.append(answer)
                return

            for letter in phone[digits[loc]]:
                temp_ans = answer + letter
                rec(loc + 1, temp_ans)
        
        rec(0, '')
        
        return res
                