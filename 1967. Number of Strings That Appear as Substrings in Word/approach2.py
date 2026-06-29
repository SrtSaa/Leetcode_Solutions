from typing import List

# Approach 2: Using a nested loop to check for substrings
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n = len(word)
        count = 0
        for pattern in patterns:
            i = 0
            m = len(pattern)
            while i + m <= n:
                flag = True
                for j in range(m):
                    if word[i + j] != pattern[j]:
                        flag = False
                        break
                if flag:
                    count += 1
                i += 1
        return count



# Time Complexity: O(n * m * k), where n is the length of the word, m is the average length of the patterns, and k is the number of patterns. In the worst case, we may have to check each character of the word for each pattern.
# Space Complexity: O(1), as we are using a constant amount of extra space.