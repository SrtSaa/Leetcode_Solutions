from typing import List

# Approach 1: Binary Search
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def bs(nums, x):
            l, r = 0, len(nums)-1
            while l<=r:
                mid = l + (r-l)//2
                if nums[mid] > x:   
                    r = mid - 1
                elif nums[mid] < x: 
                    l = mid + 1
                else:
                    return True
            return False

        m, n = len(nums1), len(nums2)
        if m>n:
            self.getCommon(nums2, nums1)
        for item in nums1:
            if bs(nums2, item):
                return item
        return -1


# Time Complexity: O(m log n), where m and n are the lengths of nums1 and nums2 respectively.
# Space Complexity: O(1), as we are using only constant extra space.