from typing import List

# Approach 1: Prefix Sum
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        for num in gain:
            altitude.append(altitude[-1] + num)
        return max(altitude)


# Time Complexity: O(n) as we need to iterate through the gain array once to calculate the altitude and then find the maximum altitude.
# Space Complexity: O(n) as we are storing the altitude at each point in a separate list.