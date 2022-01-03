class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        first_key = [0] * 26
        
        for letter in s:
            first_key[ord(letter) - ord("a")] += 1
        
        second_key = [0] * 26
        for letter in t:
            second_key[ord(letter) - ord("a")] += 1
        
        
        return first_key == second_key