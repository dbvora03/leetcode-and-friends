class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        answer = []  
        size = 1
        total_sum = 0
        
        while size < n:
            answer.append(size)
            total_sum += size
            size += 1

        
        answer.insert(0, -1 * total_sum)
        return answer