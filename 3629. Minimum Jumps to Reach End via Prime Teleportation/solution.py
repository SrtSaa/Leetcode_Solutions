from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        def make_sieve(n):
            primes = [True]*(n+1)
            primes[0] = primes[1] = False
            for i in range(n):
                if primes[i]:
                    for j in range(i*i, n+1, i):
                        primes[j] = False
            return primes
        
        n = len(nums)
        d = defaultdict(list)
        maxi = max(nums)
        primes = make_sieve(maxi)
        for i in range(n):
            d[nums[i]].append(i)
        
        vis = [0]*n
        q = deque([])
        q.append((0, 0))
        vis[0] = 1
        while q:
            idx, step = q.popleft()
            if idx == n-1:
                return step
            if idx-1 >= 0 and vis[idx-1] == 0:
                q.append((idx-1, step+1))
                vis[idx-1] = 1
            
            if idx+1 < n and vis[idx+1] == 0:
                q.append((idx+1, step+1))
                vis[idx+1] = 1
            
            if primes[nums[idx]] == 1:
                prime = nums[idx]
                for multiple in range(prime, maxi+1, prime):
                    if multiple in d:
                        for ele in d[multiple]:
                            if vis[ele] == 0:
                                q.append((ele, step+1))
                                vis[ele] = 1
                        # del d[multiple]
            primes[nums[idx]] = 0


# Time Complexity: O(n * log(log(max(nums)))) where n is the length of the input array and max(nums) is the maximum value in the input array. The sieve of Eratosthenes runs in O(n log log n) time, and the BFS traversal takes O(n) time in the worst case.
# Space Complexity: O(n + max(nums)) where n is the length of the input array and max(nums) is the maximum value in the input array. The space is used for the visited array, the queue for BFS, and the sieve of Eratosthenes.
