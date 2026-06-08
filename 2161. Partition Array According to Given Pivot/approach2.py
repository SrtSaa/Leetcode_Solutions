from typing import List

# Approach 2: Using Extra Space
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller, equal, greater = [], [], []
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        smaller.extend(equal)
        smaller.extend(greater)
        for i in range(len(nums)):
            nums[i] = smaller[i]
        return nums


# Time Complexity: O(n)
# Space Complexity: O(n)