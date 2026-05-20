from typing import List

# Approach 3: Hash Set
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = s1.intersection(s2)
        if len(s3)==0:
            return -1
        return min(s3)


# Time Complexity: O(m + n), as we are iterating through both arrays to create the hash sets and then finding the intersection.
# Space Complexity: O(m + n), as we are using extra space to store the hash sets.