class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]
        
        import heapq
        stones = [-x for x in stones]
        heapq.heapify(stones)
                
        while len(stones) > 1:
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            
            if y != x:
                y -= x
                heapq.heappush(stones, -1 * y)

        return stones[0] * -1 if stones else 0