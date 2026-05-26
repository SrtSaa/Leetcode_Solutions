from typing import List

class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            #print(l, r, mid)
            if nums[mid] < t:
                if nums[l] < nums[r]:  l = mid + 1
                else:
                    if nums[l] <= t and nums[mid] < nums[r]:
                        r = mid - 1
                    else:   l = mid + 1
            elif nums[mid] > t:
                if nums[l] < nums[r]:  r = mid - 1
                else:
                    if nums[r] >= t and nums[mid] > nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
            else:
                return mid
        return -1


# Time complexity: O(log(n))
# Space complexity: O(1)