from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = False
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if flag:
                    return False
                flag = True
        if flag and nums[n-1] > nums[0]:
            return False
        return True

# Time Complexity: O(n) where n is the length of the input array.
# Space Complexity: O(1) since we are using only a constant amount of extra space