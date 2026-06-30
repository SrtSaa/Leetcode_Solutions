# Approach 1: Sliding Window
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {'a': 0, 'b': 0, 'c': 0}
        l = r = count = 0
        n = len(s)
        while r < n:
            freq[s[r]] += 1

            while freq['a']>0 and freq['b']>0 and freq['c']>0:
                count += n - r
                freq[s[l]] -= 1
                l += 1

            r += 1
        return count



# Time Complexity: O(n)
# Space Complexity: O(1)