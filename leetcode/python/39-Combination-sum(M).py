class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        final = []
        
        def rec(balance, answer):
                        
            if balance == 0:
                
                answer.sort()
                if answer not in final:
                    final.append(answer)
                return
            if balance < 0:
                return 
            
            for candidate in candidates:
                temp_answer = answer.copy()
                
                if balance - candidate >= 0:
                    
                    temp_answer.append(candidate)                    

                    rec(balance - candidate, temp_answer)
                    
        rec(target, [])
        return list(final)