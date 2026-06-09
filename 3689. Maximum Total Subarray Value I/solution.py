from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums)-min(nums)) * k


# Time complexity: O(n) to find the maximum and minimum values in the list.
# Space complexity: O(1) since we are using a constant amount of space to store