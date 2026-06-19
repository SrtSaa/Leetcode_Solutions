from typing import List

# Approach 2: Iterative
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        ans = 0
        for num in gain:
            curr += num
            ans = max(ans, curr)
        return ans


# Time Complexity: O(n) as we need to iterate through the gain array once to calculate the altitude and find the maximum altitude.
# Space Complexity: O(1) as we are using only a constant amount of space to store the current altitude and the maximum altitude.