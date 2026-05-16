from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while(l<r):
            mid = (l+r) >> 1
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
    

# Time complexity: O(log n) as we are using binary search
# Space complexity: O(1) as we are using constant space to store the pointers and mid value.