class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counts = {}
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        
        
        import heapq
        
        heap = list(counts.items())
        
        heap = [(-j, i) for i, j in heap]
        heapq.heapify(heap)

        answer = []
        for i in range(k):
            value = heapq.heappop(heap)
            answer.append(value[1])

        return answer