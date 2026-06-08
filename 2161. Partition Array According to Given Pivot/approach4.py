from typing import List

# Approach 4: Two Pointers
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [0]*n
        smaller = 0
        greater = n - 1
        for i, j in zip(range(n), range(n-1, -1, -1)):
            if nums[i] < pivot:
                ans[smaller] = nums[i]
                smaller += 1
            if nums[j] > pivot:
                ans[greater] = nums[j]
                greater -= 1
        for i in range(smaller, greater+1):
            ans[i] = pivot
        for i in range(n):
            nums[i] = ans[i]
        return nums



# Time Complexity: O(n)
# Space Complexity: O(n)