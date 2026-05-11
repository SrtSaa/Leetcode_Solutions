from typing import List

# Approach 3: Using String Conversion
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for digit in str(num):
                ans.append(int(digit))
        return ans


# Time complexity: O(n*log(m)), where n is the length of nums and m is the maximum number in nums.
# Space complexity: O(1)