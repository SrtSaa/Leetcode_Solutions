from typing import List

# Approach 1: Brute Force
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        for num in nums:
            if num < pivot:
                ans.append(num)
        for num in nums:
            if num == pivot:
                ans.append(num)
        for num in nums:
            if num > pivot:
                ans.append(num)
        for i in range(len(nums)):
            nums[i] = ans[i]
        return ans


# Time Complexity: O(n)
# Space Complexity: O(n)