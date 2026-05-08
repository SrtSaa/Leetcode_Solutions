from collections import deque
from typing import List


# Approach 1: Using queue
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # in python, there is no separate queue/stack data structure, 
        # these can be implemented using deque
        n = len(nums)
        k = k % n
        dq = deque(nums) 
        for _ in range(k):
            x = dq.pop()
            dq.appendleft(x)
        for i in range(len(nums)):
            nums[i] = dq[i]


# Time complexity: O(n)
# Space complexity: O(n) for deque