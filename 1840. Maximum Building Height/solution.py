from typing import List

class Solution:
    def maxBuilding(self, n: int, rest: List[List[int]]) -> int:
        rest.append([1, 0])
        rest.sort()
        m = len(rest)
        if rest[m-1][0] != n:
            rest.append([n, n-1])
            m += 1

        for i in range(m-2, -1, -1):
            dist = rest[i+1][0] - rest[i][0]
            rest[i][1] = min(rest[i][1], rest[i+1][1]+dist)
        for i in range(1, m):
            dist = rest[i][0] - rest[i-1][0]
            rest[i][1] = min(rest[i][1], rest[i-1][1]+dist)
        
        ans = 0
        for i in range(1, m):
            dist = rest[i][0] - rest[i-1][0]
            curr_max = (rest[i][1] + rest[i-1][1] + dist) // 2
            ans = max(ans, curr_max)
        
        return ans



# Time Complexity: O(m log m), where m is the length of the rest list. The sorting step takes O(m log m) time, and the subsequent loops each take O(m) time. Therefore, the overall time complexity is dominated by the sorting step.
# Space Complexity: O(1), as we are modifying the input list in place and using a constant amount of extra space for variables, ignoring the space used for storing the input list.