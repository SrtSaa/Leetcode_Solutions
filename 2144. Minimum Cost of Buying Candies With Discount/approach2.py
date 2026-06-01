from typing import List

# Approach 2: Using Frequency Array
class Solution:
    def minimumCost(self, costs: List[int]) -> int:
        mx = max(costs)
        freq = [0]*(mx+1)
        for cost in costs:
            freq[cost] += 1
        ans = 0
        rem = 0
        for cost in range(mx, 0, -1):
            if freq[cost] == 0: continue
            if rem == 2:
                freq[cost] -= 1
            elif rem == 1:
                freq[cost] -= 2
                ans += cost
            rem = freq[cost] % 3
            ans += (freq[cost]//3) * 2 * cost + rem * cost
        return ans



# Time Complexity: O(n + m) where n is the number of candies and m is the maximum cost of a candy
# Space Complexity: O(m) where m is the maximum cost of a candy due to the frequency array