from typing import List
import math

# Solution 1: Using a set to store the prefixes of the first array 
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s = set()
        ans = 0
        for num in arr1:
            while num > 0:
                if num in s:
                    break
                s.add(num)
                num = num // 10
        for num in arr2:
            while num > 0 and int(math.log(num, 10))+1 > ans:
                if num in s:
                    ans = max(ans, int(math.log(num, 10))+1)
                    break
                num = num // 10

        return ans
        

# Time Complexity: O(n * log(m)) where n is the length of the longer array and m is the maximum number in the arrays (since we are dividing by 10 to get the prefixes).
# Space Complexity: O(n * log(m)) in the worst case if all numbers in the first array are unique and have different prefixes.