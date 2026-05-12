from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0]-x[1])
        curr, energy = 0, 0
        for ac, mn in tasks:
            need_to_add = max(0, mn - curr)
            energy += need_to_add
            curr = curr + need_to_add - ac
        return energy


# Time complexity: O(nlogn) due to sorting
# Space complexity: O(1) since we are sorting in place and using only a constant amount of extra space.