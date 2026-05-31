from typing import List

# Approach 2: Sorting
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid
        return True 


# Time Complexity: O(n log n) due to the sorting step, where n is the number of asteroids. The iteration through the sorted list takes O(n) time.
# Space Complexity: O(1) if we ignore the space used by the sorting algorithm