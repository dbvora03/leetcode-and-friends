class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for number in nums:
            if number in dup:
                return True
            else:
                dup.add(number)
        return False
            