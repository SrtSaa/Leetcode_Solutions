from typing import List

# Approach 2: Counting Sort
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx = max(costs)
        freq = [0] * (mx + 1)
        for cost in costs:
            freq[cost] += 1
        count = 0
        for i in range(1, mx+1):
            if freq[i] == 0:
                continue
            if i > coins:
                break
            buy = min(freq[i], coins//i)
            count += buy
            coins -= i*buy
        return count 



# Time Complexity: O(n + m) where n is the length of costs and m is the maximum cost in costs.
# Space Complexity: O(m) where m is the maximum cost in costs.