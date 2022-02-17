class Solution:
    def reverseBits(self, n: int) -> int:
        
        new_number = 0
        
        for i in range(32):
            
            bit = n & 1
            n = n >> 1
            
            new_number = (new_number << 1) | bit
            
        return new_number












