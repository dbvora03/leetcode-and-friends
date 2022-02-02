class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        counts = {}
        
        for i, row in enumerate(mat):
            count = 0
            for number in row:
                if number == 1:
                    count += 1
            
            counts[i] = count
        
        import heapq
        heap = []
        
        for key in counts:
            heapq.heappush(heap, (counts[key], key))
        
        answer = []
        for _ in range(k):
            value = heapq.heappop(heap)
            answer.append(value[1])
        
        return answer