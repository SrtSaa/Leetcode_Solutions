from typing import List

# Approach 2: Tabulation
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        t = [float('-inf')]*n
        t[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if(abs(nums[i] - nums[j]) <= target):
                    t[i] = max(t[i], 1 + t[j])

        
        if t[0] < 0:
            return -1
        return t[0]
            
          
# Time Complexity: O(n^2)
# Space Complexity: O(n)       