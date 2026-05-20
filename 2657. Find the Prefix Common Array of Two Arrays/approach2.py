from typing import List

# Approach 2: Using Two Sets and a Counter
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        seenA, seenB = set(), set()
        count = 0
        for i in range(len(A)):
            if A[i] in seenB:
                count += 1
            seenA.add(A[i])
            if B[i] in seenA:
                count += 1
            seenB.add(B[i])
            ans.append(count)
        return ans


# Time Complexity: O(n) where n is the length of the input arrays A and B.
# Space Complexity: O(n) for the sets used to store the seen elements of A and B.