class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [0]*26
        upper = [0]*26

        for ch in word:
            if ch.islower():
                lower[ord(ch)-ord('a')] += 1
            else:
                upper[ord(ch)-ord('A')] += 1
        
        count = 0
        for i in range(26):
            if lower[i]>0 and upper[i]>0:
                count += 1
        
        return count


# Time Complexity: O(n) 
# Space Complexity: O(26) = O(1)