class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq
        
        
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
    
        
        val = 0
        while k > 0:
            val = heapq.heappop(maxHeap)
            k -= 1
        
        return val * -1