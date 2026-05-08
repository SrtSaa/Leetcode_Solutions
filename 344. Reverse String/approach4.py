from typing import List

# Approach 4 (Optimal): using two pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# Time complexity: O(n/2) 
# Space complexity: O(1) for in-place swapping
            

            