# Approach 1: Check All Rotations
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        m = len(s)
        n = len(goal)
        if m!=n:
            return False
        for j in range(n):
            i = 0
            while i<m:
                if s[i] == goal[j%n]:
                    i += 1
                    j += 1
                else:
                    j -= 1
                    break
            if i == m:
                return True
        return False

# Time Complexity: O(n^2)
# Space Complexity: O(1)
