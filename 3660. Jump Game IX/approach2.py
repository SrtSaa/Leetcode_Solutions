from typing import List

# Approach 2: In-place Modification of Prefix Max
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixMax = [0] * len(nums)
        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i-1], nums[i])
        
        suffixMin = nums[n-1]
        for i in range(n-2, -1, -1):
            if prefixMax[i] > suffixMin:
                prefixMax[i] = prefixMax[i+1]
            suffixMin = min(nums[i], suffixMin)
        
        return prefixMax


# Time Complexity: O(n)
# Space Complexity: O(n)