from typing import List


# Approach 2: Using two loops
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n
        new_nums = []
        for i in range(k, n):
            new_nums.append(nums[i])
        for i in range(k):
            new_nums.append(nums[i])
        for i in range(n):
            nums[i] = new_nums[i]


# Time complexity: O(n)
# Space complexity: O(n) for new_nums
