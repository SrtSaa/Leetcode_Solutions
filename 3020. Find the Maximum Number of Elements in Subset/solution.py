from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        mx = max(nums)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        ans = 1
        
        for num in freq:
            size = 0
            if num == 1:
                size = freq[1]
                if not(freq[1] & 1):
                    size -= 1
            else:
                while freq[num] >= 2 and num*num in freq:
                    size += 2
                    num = num ** 2
                size += 1
            ans = max(ans, size)
        
        return ans
    


# Time complexity: O(n + d.loglog(M)), where n is the number of elements in nums and d is the number of distinct elements in nums and M is the maximum element in nums
# Space complexity: O(d), where d is the number of distinct elements in nums