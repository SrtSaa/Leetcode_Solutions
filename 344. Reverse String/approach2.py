from typing import List
from collections import deque

# Approach 2: Using queue
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        queue = deque()
        for i in range(n):
            queue.append(s[i])
        for i in range(n):
            s[i] = queue.pop()

# Time complexity: O(n)
# Space complexity: O(n) for queue
        



            