class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        answer = []
        inserted = False
        for i, a in enumerate(intervals):            
            if not inserted and newInterval[0] < a[0]:
                answer.append(newInterval)
                inserted = True
            answer.append(a)
        
        if not inserted:
            answer.append(newInterval)
                    
        res = [answer[0]]
        
        for interval in answer[1:]:
            if res[-1][1] >= interval[0]:
                res[-1] = [min(interval[0], res[-1][0]), max(interval[1], res[-1][1])]
            else:
                res.append(interval)
        
        return res
        
        
    