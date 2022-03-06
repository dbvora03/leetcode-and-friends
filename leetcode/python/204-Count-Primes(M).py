class Solution:
    def countPrimes(self, n: int) -> int:
        
        ans = 0
        
        if n <= 1:
            return 0
        
        primes = [True] * (n + 1)
        
        primes[0] = primes[1] = False
        
        for i in range(2, n):
            if primes[i]:
                ans += 1
                for j in range(2*i, n, i):
                    primes[j] = False
        
        return ans