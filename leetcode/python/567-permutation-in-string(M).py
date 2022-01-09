class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        one_key = [0] * 26
        for letter in s1:
            one_key[ord(letter) - ord("a")] += 1
        
        
        for i in range(len(s2) - len(s1) + 1):
            the_word = s2[i:(i+len(s1))]
            two_key = [0] * 26
            for letter in the_word:
                two_key[ord(letter) - ord("a")] += 1
            
            if two_key == one_key:
                return True
        
        return False