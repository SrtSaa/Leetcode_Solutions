from typing import List

# Approach 3: Tabulation (Optimized)
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0]*n
        for i in range(n):
            if i>0 and dp[i] == 0:
                continue
            for j in range(i+1, n):
                if abs(nums[j]-nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
            # print(i, dp)
        if dp[n-1] == 0:
            return -1 
        else: 
            return dp[n-1]