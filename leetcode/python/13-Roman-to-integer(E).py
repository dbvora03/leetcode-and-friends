class Solution:
    def romanToInt(self, s: str) -> int:
        
        answer = 0
        
        number_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        numbers_in_arr = [number_map[x] for x in s]
        
        for i in range(len(numbers_in_arr) - 1):
            if numbers_in_arr[i] < numbers_in_arr[i + 1]:
                answer -= numbers_in_arr[i]
            else:
                answer += numbers_in_arr[i]
        
        return answer + numbers_in_arr[-1]