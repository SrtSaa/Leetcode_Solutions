from typing import List

# Approach 2: Two Pointers
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                i+=1
            elif nums2[j] < nums1[i]:
                j+=1
            else:
                return nums1[i]
        return -1
    

# Time Complexity: O(m + n), where m and n are the lengths of nums1 and nums2 respectively. As we are iterating through both arrays at most once.
# Space Complexity: O(1), as we are using only constant extra space.