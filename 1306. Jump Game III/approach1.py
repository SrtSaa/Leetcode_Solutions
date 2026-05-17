from typing import List
from collections import deque

# Approach 1: BFS
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [False]*n
        q = deque([start])
        vis[start] = True
        while q:
            idx = q.popleft()
            if arr[idx] == 0:
                return True
            l, r = idx-arr[idx], idx+arr[idx]
            if l >= 0 and not vis[l]:
                q.append(l)
                vis[l] = True
            if r < n and not vis[r]:
                q.append(r)
                vis[r] = True

        return False


# Time Complexity: O(n) as each index is visited at most once.
# Space Complexity: O(n) for the queue and visited array.