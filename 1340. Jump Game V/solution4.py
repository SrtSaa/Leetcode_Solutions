from collections import deque
from typing import List

# Solution 4: Topological Sort + Iterative DP
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        
        # 1. Build prevGreater using Monotonic Stack
        stack = []
        prevGreater = [-1] * n
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                prevGreater[i] = stack[-1]
            stack.append(i)

        # 2. Build nextGreater using Monotonic Stack
        stack = []
        nextGreater = [n] * n
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                nextGreater[i] = stack[-1]
            stack.append(i)
        
        # 3. Calculate In-Degrees for Topological Sort
        in_degree = [0] * n
        for i in range(n):
            p = prevGreater[i]
            if p != -1 and i - p <= d:
                in_degree[p] += 1
                
            nx = nextGreater[i]
            if nx != n and nx - i <= d:
                in_degree[nx] += 1
                
        # 4. Iterative DP using a Queue (Kahn's Algorithm)
        dp = [1] * n
        # Start with all local minimums (elements that have nothing pushing into them)
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            i = queue.popleft()
            
            # Push up to prevGreater
            p = prevGreater[i]
            if p != -1 and i - p <= d:
                dp[p] = max(dp[p], dp[i] + 1)
                in_degree[p] -= 1
                if in_degree[p] == 0:
                    queue.append(p)
                    
            # Push up to nextGreater
            nx = nextGreater[i]
            if nx != n and nx - i <= d:
                dp[nx] = max(dp[nx], dp[i] + 1)
                in_degree[nx] -= 1
                if in_degree[nx] == 0:
                    queue.append(nx)

        return max(dp)


# Time complexity: O(n) for building the monotonic stacks, O(n) for calculating in-degrees, and O(n) for the topological sort, resulting in an overall time complexity of O(n).
# Space complexity: O(n) for the monotonic stacks, the prevGreater and nextGreater arrays, the in_degree array, the dp array, and the queue used for topological sorting.