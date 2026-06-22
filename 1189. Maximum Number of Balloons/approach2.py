import math

# Approach 2: Hash Map
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        target_freq = {}
        text_freq = {}
        for ch in target:
            target_freq[ch] = target_freq.get(ch, 0) + 1
        for ch in text:
            text_freq[ch] = text_freq.get(ch, 0) + 1
        ans = math.inf
        for ch in target_freq:
            if ch not in text_freq:
                return 0
            ans = min(ans, text_freq[ch]//target_freq[ch])
        return ans


# Time Complexity: O(n + m) where n is the length of text and m is the length of target
# Space Complexity: O(1) as the size of the hash maps is limited by the number of unique characters in target and text, which is at most 26 for lowercase English letters.