from typing import List

# Approach 1: Prefix Max and Suffix Min
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixMax = [0] * len(nums)
        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i-1], nums[i])
        
        ans = [0]*n
        ans[n-1] = prefixMax[n-1]
        suffixMin = nums[n-1]
        for i in range(n-2, -1, -1):
            if prefixMax[i] <= suffixMin:
                ans[i] = prefixMax[i]
            else:
                ans[i] = ans[i+1]
            suffixMin = min(nums[i], suffixMin)
        
        return ans


# Time Complexity: O(n)
# Space Complexity: O(n)