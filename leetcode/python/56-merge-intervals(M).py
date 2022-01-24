class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        
        answer = [intervals[0]]
        
        for number in range(1, len(intervals)):
            
            if answer[-1][1] >= intervals[number][0]:
                answer[-1] = [answer[-1][0], max(answer[-1][1], intervals[number][1])]
            else:
                answer.append(intervals[number])
        
        return answer