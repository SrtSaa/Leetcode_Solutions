from collections import deque

# Solution 1: BFS
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] != '0':
            return False
        vis = [False]*n
        dq = deque([0])
        vis[0] = True
        while dq:
            idx = dq.popleft()
            for i in range(idx+minJump, min(idx+maxJump+1, n)):
                if s[i] == '0' and not vis[i]:
                    if i == n-1:
                        return True
                    dq.append(i)
                    vis[i] = True
        return False


# Time complexity: O(n*(maxJump-minJump))
# Space complexity: O(n)