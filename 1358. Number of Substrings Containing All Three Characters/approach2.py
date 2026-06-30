# Approach 2: Sliding Window
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        for i in range(len(s)):
            freq[s[i]] = i
            count += 1 + min(freq['a'], freq['b'], freq['c']) 
        return count


# Time Complexity: O(n)
# Space Complexity: O(1)