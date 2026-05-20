from typing import List

# Approach 1: Using Set Intersection
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        s1, s2 = set(), set()
        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])
            ans.append(len(s1.intersection(s2)))
        return ans

# Time Complexity: O(n^2) in the worst case due to the intersection operation inside the loop.
# Space Complexity: O(n) for the sets used to store the elements of A and B