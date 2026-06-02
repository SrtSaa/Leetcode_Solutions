from math import inf
from typing import List

# Approach 2: Optimized with Two Passes
class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        
        def solve(start1, duration1, start2, duration2):
            finishFirst = inf
            for i in range(len(start1)):
                finishFirst = min(finishFirst, start1[i]+duration1[i])
            finishLast = inf
            for i in range(len(start2)):
                finishLast = min(finishLast, max(finishFirst, start2[i]) + duration2[i])
            return finishLast
        
        land_first = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        water_first = solve(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(land_first, water_first)



# Time Complexity: O(n + m), where n and m are the lengths of landStartTime and waterStartTime respectively.
# Space Complexity: O(1), as we are using only a constant amount of extra space.