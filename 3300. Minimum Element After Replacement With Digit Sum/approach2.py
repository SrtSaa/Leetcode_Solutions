from typing import List

# Approach 2: Precompute digit sums for numbers up to the maximum possible value
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for n in nums:
            ans = min(ans, (n//10000)+(n//1000)%10+(n//100)%10+(n//10)%10+n%10)
        return ans

# Time Complexity: O(n), where n is the length of the input array. This is because we need to iterate through each element in the array once to calculate the sum of its digits using the precomputed values.
# Space Complexity: O(1), as we are using only a constant amount of extra space to store the minimum sum and the current sum while calculating the digit sum.