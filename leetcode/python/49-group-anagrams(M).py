class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        
        for word in strs:
            
            word_key = [0] * 26
            for letter in word:
                word_key[ord(letter) - ord("a")] += 1
            
            res[tuple(word_key)].append(word)
        return res.values()
                