from typing import List

# Solution 2: Using a trie to store the prefixes of the first array
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}
        for num in arr1:
            s = str(num)
            curr = trie
            for digit in s:
                if digit not in curr:
                    curr[digit] = {}
                curr = curr[digit]
        
        ans = 0
        for num in arr2:
            s = str(num)
            curr = trie
            size = 0
            for digit in s:
                if digit not in curr:
                    break
                curr = curr[digit]
                size += 1
            ans = max(ans, size)

        return ans
    


# Time Complexity: O(n * log(m)) where n is the length of the longer array and m is the maximum number in the arrays (since we are converting numbers to strings to get the prefixes).
# Space Complexity: O(n * log(m)) in the worst case if all numbers in the first array are unique and have different prefixes.