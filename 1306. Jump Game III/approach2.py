from typing import List

# Approach 2: DFS
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [False]*n
        
        def dfs(idx):
            if arr[idx] == 0:
                return True
            l, r = idx-arr[idx], idx+arr[idx]
            if l >= 0 and not vis[l]:
                vis[l] = True
                if dfs(l):
                    return True
            if r < n and not vis[r]:
                vis[r] = True
                if dfs(r):
                    return True
            return False

        vis[start] = True
        return dfs(start)

# Time Complexity: O(n) as each index is visited at most once.
# Space Complexity: O(n) for the visited array and recursion stack.