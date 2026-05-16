from typing import List

# Approach 2: sort the array and check the elements
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        size = len(nums)
        n = size - 1
        for i in range(n):
            if nums[i] != i+1:
                return False
        if nums[n] != n:
            return False
        return True

# Time Complexity: O(n log n) because of the sorting step
# Space Complexity: O(1) because we are not using any extra space