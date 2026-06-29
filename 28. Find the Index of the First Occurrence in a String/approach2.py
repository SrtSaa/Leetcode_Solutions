# Approach 2: KMP Algorithm
class Solution:
    def strStr(self, text: str, target: str) -> int:
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
                    length = lps[length-1]
            
        i, j = 0, 0
        while i<n:
            if text[i] == target[j]:
                i += 1
                j += 1
                if j == m:
                    return i-j
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
        return -1
        
        

# Time Complexity: O(n+m) where n is the length of text and m is the length of target
# Space Complexity: O(m) where m is the length of target