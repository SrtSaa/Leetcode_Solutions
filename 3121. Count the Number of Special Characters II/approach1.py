# Approach 1: Two Arrays
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [-1] * 26
        upper = [-1] * 26
        for i in range(len(word)):
            ch = word[i]
            if ch.islower():
                lower[ord(ch) - ord('a')] = i
            else:
                if upper[ord(ch) - ord('A')] == -1:
                    upper[ord(ch) - ord('A')] = i
        
        count = 0
        for i in range(26):
            if lower[i] > -1 and upper[i] > -1 and lower[i] < upper[i]:
                count += 1
        return count


# Time Complexity: O(n) where n is the length of the input string `word`.
# Space Complexity: O(1) since the size of the `lower` and `upper` arrays is fixed at 26, regardless of the input size.