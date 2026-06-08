from typing import List

# Approach 3: Three Pointers
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        smaller, equal = 0, 0
        for num in nums:
            if num < pivot:
                smaller += 1
            elif num == pivot:
                equal += 1
        ans = [0]*n
        x = 0
        y = smaller
        z = smaller + equal
        for i in range(n):
            if nums[i] < pivot:
                ans[x] = nums[i]
                x += 1
            elif nums[i] > pivot:
                ans[z] = nums[i]
                z += 1
            else:
                ans[y] = nums[i]
                y += 1
        for i in range(n):
            nums[i] = ans[i]
        return nums



# Time Complexity: O(n)
# Space Complexity: O(n)