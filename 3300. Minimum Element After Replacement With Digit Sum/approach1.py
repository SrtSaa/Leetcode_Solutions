from typing import List

# Approach 1: 
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for num in nums:
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10
            ans = min(ans, sum)
        return ans


# Time Complexity: O(n * log(m)), where n is the length of the input array and m is the maximum element in the array. This is because we need to iterate through each element in the array and calculate the sum of its digits, which takes O(log(m)) time.
# Space Complexity: O(1), as we are using only a constant amount of extra space to store the minimum sum and the current sum while calculating the digit sum.