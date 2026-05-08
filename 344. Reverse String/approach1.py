from typing import List

# Approach 1: Using extra array
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        new_arr = []
        for i in range(n-1, -1, -1):
            new_arr.append(s[i])
        for i in range(n):
            s[i] = new_arr[i]

# Time complexity: O(n)
# Space complexity: O(n) for new_arr

            