from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while(l<r):
            mid = (l+r) >> 1
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        return nums[r]


# Time complexity: O(log n) in the average case, O(n) in the worst case when all elements are the same.
# Space complexity: O(1) since we are using only a constant amount of extra space.