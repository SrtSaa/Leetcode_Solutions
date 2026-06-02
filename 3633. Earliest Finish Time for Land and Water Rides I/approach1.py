from math import inf
from typing import List

# Approach 1: Brute Force
class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        
        res = inf
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                landFirst = landStartTime[i] + landDuration[i]
                waterLast = max(landFirst, waterStartTime[j]) + waterDuration[j]
                res = min(res, waterLast)

                waterFirst = waterStartTime[j] + waterDuration[j]
                landLast = max(waterFirst, landStartTime[i]) + landDuration[i]
                res = min(res, landLast)
        
        return res


# Time Complexity: O(n * m), where n and m are the lengths of landStartTime and waterStartTime respectively.
# Space Complexity: O(1), as we are using only a constant amount of extra space