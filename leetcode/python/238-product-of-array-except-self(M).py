class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zero = False
        
        for number in nums:
            if number == 0:
                if zero:
                    return [0] * len(nums)
                else:
                    zero = True
            else:
                mult *= number
        
        if zero:
            return [0 if n != 0 else mult for n in nums]
        else:
            return [mult // n for n in nums]