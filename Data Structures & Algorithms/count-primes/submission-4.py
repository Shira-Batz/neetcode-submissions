class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        primes = [True] * n
        for i in range (2, n):
            if primes[i]:
                count += 1
                for j in range (i*i, n, i):
                    primes[j] = False
        return count