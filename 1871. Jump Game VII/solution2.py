from collections import deque

# Solution 2: BFS with pruning
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] != '0':
            return False
        dq = deque([0])
        for i in range(minJump, n):
            if s[i] != '0': 
                continue
            while dq and ( i < dq[0] + minJump or i > dq[0] + maxJump):
                dq.popleft()
            if not dq:
                return False
            if i >= dq[0] + minJump:
                if i == n-1: 
                    return True
                dq.append(i)
        return False
                

# Time complexity: O(n)
# Space complexity: O(n)
