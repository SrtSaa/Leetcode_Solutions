from typing import List

# Approach 1: Sort and Greedy
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if cost <= coins:
                count += 1
                coins -= cost
            else:
                break
        return count


# Time Complexity: O(n log n) due to sorting the costs array, where n is the number of ice cream bars.
# Space Complexity: O(1) if we ignore the space used for sorting, otherwise O(n) for the sorted array.