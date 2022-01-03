class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        min = math.floor(len(nums) / 3)
        answer = []
        
        cache = {}
        
        for number in nums:
            if number not in cache:
                cache[number] = 0
    
            cache[number] += 1
        
        for key in cache:
            if cache[key] > min:
                answer.append(key)
        
        return answer