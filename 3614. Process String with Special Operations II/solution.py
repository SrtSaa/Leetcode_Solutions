class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0 
        for ch in s:
            if ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2
            elif ch == '%':
                continue
            else:
                length += 1
        if length < k + 1:
            return '.'
        for i in range(len(s)-1, -1, -1):
            if s[i] == '*':
                length += 1
            elif s[i] == '#':
                if k >= length//2:
                    k = k - length // 2
                length = length // 2
            elif s[i] == '%':
                k = length - k -1
            else:
                if length == k + 1:
                    return s[i]
                length -= 1


# Time Complexity: O(n), where n is the length of the string s. We traverse the string twice, once to calculate the final length and once to find the k-th character. 
# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.