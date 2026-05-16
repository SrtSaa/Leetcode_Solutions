from typing import List

# Approach 3: using a count array to count the occurrences of each number in the array
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        count = [0]*n
        for num in nums:
            if num >= n:
                return False
            count[num] += 1
            if num < n-1 and count[num] > 1:
                return False
            if num == n-1 and count[num] > 2:
                return False
        return True

# Time Complexity: O(n) because we are iterating through the array only once
# Space Complexity: O(n) because we are using an additional array to count the occurrences of each number