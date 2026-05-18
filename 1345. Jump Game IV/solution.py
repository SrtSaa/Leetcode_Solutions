from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        mp = defaultdict(list)

        for i in range(n):
            mp[arr[i]].append(i)
        
        vis = [False]*n
        q = deque([(0, 0)])
        vis[0] = True

        while q:
            idx, jump = q.popleft()
            if idx == n-1:
                return jump
            if idx-1 >= 0 and not vis[idx-1]:
                q.append((idx-1, jump+1))
                vis[idx-1] = True
            if idx+1 < n and not vis[idx+1]:
                q.append((idx+1, jump+1))
                vis[idx+1] = True
            for i in mp[arr[idx]]:
                if i != idx and not vis[i]:
                    q.append((i, jump+1))
                    vis[i] = True
            mp[arr[idx]].clear()

# Time Complexity: O(n) because each index is visited at most once, and the inner loop for the same value is also visited at most once due to the clearing of the map.
# Space Complexity: O(n) for the queue and the visited array, and O(n) for the map in the worst case.