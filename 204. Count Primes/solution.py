class Solution:
    def countPrimes(self, n: int) -> int:
        def make_sieve(n):
            primes = [True]*(n+1)
            primes[0] = primes[1] = False
            for i in range(n):
                if primes[i]:
                    for j in range(i*i, n+1, i):
                        primes[j] = False
            return primes
        
        if n < 2:
            return 0
        count = 0
        sieve = make_sieve(n)
        for i in range(n):
            if sieve[i]:
                count += 1
        return count

# Time Complexity: O(n log log n) where n is the input number. The sieve of Eratosthenes runs in O(n log log n) time.
# Space Complexity: O(n) where n is the input number. The space is used for the sieve of Eratosthenes.