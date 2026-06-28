from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) > 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]



# Time Complexity: O(nlogn) where n is the length of the array. This is due to the sorting step.
# Space Complexity: O(1) ignoring the space used for sorting, as we are modifying the array in place.