from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        for word in words:
            sum = 0 
            for ch in word:
                sum += weights[ord(ch)-ord('a')]
            sum %= 26
            ans += chr(97+25-sum)
        return ans


# Time Complexity: O(total number of characters in words)
# Space Complexity: O(1) (excluding the space for the output string)