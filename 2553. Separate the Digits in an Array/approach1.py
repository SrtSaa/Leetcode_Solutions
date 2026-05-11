from typing import List

# Approach 1: Using Modulo and Division
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            digits = []
            while num > 0:
                digits.append(num%10)
                num = num // 10
            digits.reverse()
            ans.extend(digits)
        return ans


# Time complexity: O(n*log(m)), where n is the length of nums and m is the maximum number in nums.
# Space complexity: O(log(m))