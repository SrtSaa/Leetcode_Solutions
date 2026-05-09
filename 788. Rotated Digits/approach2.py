# Approach 2: using recursion with memoization to store the result of the previous numbers
class Solution:
    def rotatedDigits(self, n: int) -> int:
        def isGood(num, mem):
            if mem[num] != -2:
                return mem[num]
            if num == 0:
                mem[num] = 0
                return 0

            rem = num % 10
            if rem == 3 or rem == 4 or rem == 7:
                flag = -1
            elif rem == 1 or rem == 8 or rem == 0:
                flag = 0
            else:    # rem is 2 or 5 or 6 or 9
                flag = 1
            
            prev_flag = isGood(num // 10, mem)
            if prev_flag == -1 or flag == -1:
                mem[num] = -1
            elif prev_flag == 0 and flag == 0: 
                mem[num] = 0
            else:
                mem[num] = 1
            return mem[num]


        
        ans = 0
        mem = [-2]*(n+1)
        for i in range(1, n+1):
            if isGood(i, mem) == 1:
                ans += 1
        return ans

# Time complexity: O(n*log(n)) where log(n) is the number of digits in n
# Space complexity: O(n) for memoization array mem