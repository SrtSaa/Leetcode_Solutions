from typing import List

# approach 1: brute force
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        def right_rotate(nums: List[int], k: int) -> None:
            def reverse(nums, start, end):
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1

            n = len(nums)
            reverse(nums, 0, n-1)
            reverse(nums, 0, k-1)
            reverse(nums, k, n-1)
        
        def calculate(nums):
            sum = 0
            for i in range(len(nums)):
                sum += i*nums[i]
            return sum
        
        ans = float('-inf')
        for _ in range(len(nums)):
            ans = max(ans, calculate(nums))
            right_rotate(nums, 1)
        return ans
    

# Time Complexity: O(n^2)
# Space Complexity: O(1)