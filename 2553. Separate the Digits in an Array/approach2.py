from typing import List

# Approach 2: Using Modulo and Division 
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            while num > 0:
                ans.append(num%10)
                num = num // 10
        ans.reverse()
        return ans


# Time complexity: O(n*log(m)), where n is the length of nums and m is the maximum number in nums.
# Space complexity: O(1)