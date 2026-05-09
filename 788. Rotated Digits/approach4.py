# Approach 4: Converting the number to string 
class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            x = str(i)
            if "3" in x or "4" in x or "7" in x:
                continue
            if "2" in x or "5" in x or "6" in x or "9" in x:
                res += 1
        return res

# Time Complexity: O(n*log(n)) where log(n) is the number of digits in n
# Space Complexity: O(log(n)) for the string representation of the number