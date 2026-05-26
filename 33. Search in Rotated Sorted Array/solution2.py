from typing import List

class Solution:
    def search(self, nums: List[int], t: int) -> int:
        def findMin(nums: List[int]) -> int:
            l = 0
            r = len(nums)-1
            while(l<r):
                mid = (l+r) >> 1
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1
            return l


        n = len(nums)
        rot = findMin(nums)
        l, r = 0, n-1
        while l<=r:
            mid = l + (r-l)//2
            real_mid = (mid + rot) % n
            if nums[real_mid] < t:
                l = mid + 1
            elif nums[real_mid] > t:
                r = mid - 1
            else:
                return real_mid
        return -1

# Time complexity: O(log(n))
# Space complexity: O(1)