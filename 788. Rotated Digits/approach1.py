# Approach 1: checking each of the digits of the number 
class Solution:
    def rotatedDigits(self, n: int) -> int:
        def isGood(num):
            flag = False
            while num>0:
                rem = num % 10
                if rem == 3 or rem == 4 or rem == 7:
                    return False
                elif rem == 2 or rem == 5 or rem == 6 or rem == 9:
                    flag = True
                num = num // 10
            return flag
        
        ans = 0
        for i in range(1, n+1):
            if isGood(i):
                ans += 1
        return ans

# Time complexity: O(n*log(n)) where log(n) is the number of digits in n
# Space complexity: O(1)