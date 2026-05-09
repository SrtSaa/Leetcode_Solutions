# Approach 2: Concatenation and Substring Check
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return s in goal+goal

# Time Complexity: O(n)
# Space Complexity: O(n)