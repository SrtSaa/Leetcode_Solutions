from typing import List

# Approach 3: Using KMP algorithm to check for substrings
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def KMP(text, target):
            m, n = len(target), len(text)
            lps = [0]*m
            length = 0
            i = 1
            while i<m:
                if target[i] == target[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length == 0:
                        i += 1
                    else:
                        length = length-1
                        # length = lps[length-1]
            
            i, j = 0, 0
            while i<n:
                if text[i] == target[j]:
                    i += 1
                    j += 1
                    if j == m:
                        return 1
                else:
                    if j == 0:
                        i += 1
                    else:
                        j = lps[j-1]
            return 0
        
        ans = 0
        for target in patterns:
            ans += KMP(word, target)
        return ans
                    

# Time Complexity: O(n + m), where n is the length of the word and m is the average length of the patterns. The KMP algorithm runs in linear time with respect to the length of the text and pattern.
# Space Complexity: O(m), where m is the length of the pattern. The space complexity is due to the lps array used in the KMP algorithm.