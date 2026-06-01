from typing import List

# Approach 1: Using Sorting
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans = 0
        i = len(cost) - 1
        while i >= 0:
            ans += cost[i]
            if i-1 >= 0:
                ans += cost[i-1]
            i -= 3
        return ans



# Time Complexity: O(nlogn) due to sorting
# Space Complexity: O(1) if we ignore the space used by sorting