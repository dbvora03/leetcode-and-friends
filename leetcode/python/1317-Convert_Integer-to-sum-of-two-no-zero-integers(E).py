class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        right, left = 1, n - 1
        
        while True:
        
            if '0' in str(right) or '0' in str(left):
                right += 1
                left -= 1
            else:
                return [left, right]