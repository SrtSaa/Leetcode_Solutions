class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        d1 = 6*minutes
        d2 = 30*hour + (0.5*minutes)
        diff = abs(d1-d2)
        return min(diff, 360-diff)

# Time Complexity: O(1)
# Space Complexity: O(1)