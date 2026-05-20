from typing import List

# Approach 3: Using a Single Set and a Counter
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        seen = set()
        count = 0
        for i in range(len(A)):
            if A[i] in seen:
                count += 1
            seen.add(A[i])
            if B[i] in seen:
                count += 1
            seen.add(B[i])
            ans.append(count)
        return ans

# Time Complexity: O(n) where n is the length of the input arrays A and B.
# Space Complexity: O(n) for the set used to store the seen elements of A and B.