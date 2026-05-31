from typing import List

# Approach 1: Simulation
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        max_mass = max(asteroids)

        while asteroids:
            pending = []
            for asteroid in asteroids:
                if mass < asteroid:
                    pending.append(asteroid)
                else:
                    mass += asteroid
                    if mass >= max_mass:
                        return True
            if len(pending) == len(asteroids):
                return False
            asteroids = pending
        
        return True



# Time Complexity: O(n^2) in the worst case, where n is the number of asteroids. This occurs when each asteroid is just slightly larger than the current mass, leading to a scenario where we have to iterate through the list of asteroids multiple times. 
# Space Complexity: O(n) in the worst case, where n is the number of asteroids. This occurs when all asteroids are larger than the initial mass, leading to a scenario where we have to store all asteroids in the pending list.