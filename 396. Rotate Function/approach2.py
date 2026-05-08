from typing import List

# approach 2: optimal
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sum, total_sum = 0, 0
        for i in range(n):
            sum += nums[i] * i
            total_sum += nums[i]
        ans = sum
        for i in range(n):
            sum = sum + total_sum - n*nums[n-1-i]
            ans = max(ans, sum)
        return ans