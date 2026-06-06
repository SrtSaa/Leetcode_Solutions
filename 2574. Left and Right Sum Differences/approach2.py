from typing import List

# Approach 2: without extra space
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rs = sum(nums)
        ls = 0
        ans = []
        for num in nums:
            rs -= num
            ans.append(abs(rs - ls))
            ls += num
        return ans


# Time complexity: O(n) 
# Space complexity: O(1)