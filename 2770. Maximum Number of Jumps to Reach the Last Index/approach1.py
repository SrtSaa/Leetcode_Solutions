from typing import List

# Approach 1: Recursion + Memoization
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        temp = [float('-inf')]*n
        
        def solve(idx):
            if temp[idx] != float('-inf'):
                return temp[idx]
            if idx == n-1:
                return 0
            
            steps = float('-inf')
            for i in range(idx+1, n):
                if abs(nums[idx]-nums[i]) <= target:
                    steps = max(steps, 1+solve(i))
            temp[idx] = steps
            return steps
        
        steps = solve(0)
        if steps < 0:
            return -1
        return steps
            
        
# Time Complexity: O(n^2)
# Space Complexity: O(n)
