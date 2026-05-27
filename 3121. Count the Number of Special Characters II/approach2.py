# Approach 2: Bit Manipulation
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = 0
        upper = 0
        for ch in word:
            if ch.islower():
                idx = ord(ch) - ord('a')
                if not upper & (1 << idx):
                    lower |= 1 << idx
                else:
                    lower &= ~(1 << idx)
            else:
                upper |= 1 << (ord(ch) - ord('A'))
        common = lower & upper
        return common.bit_count()
    

# Time Complexity: O(n) where n is the length of the input string `word`.
# Space Complexity: O(1) since we are using a constant amount of space to store the `lower` and `upper` bitmasks.