from typing import List

# Approach 1: using count method to count the occurrences of each number in the array
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        size = len(nums)
        n = size - 1
        for i in range(1, n):
            count = nums.count(i)
            if count != 1: return False
        count = nums.count(n)
        if count != 2: return False
        return True
    
# Time Complexity: O(n^2) because of the count method inside the loop
# Space Complexity: O(1) because we are not using any extra space