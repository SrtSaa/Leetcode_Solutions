# Approach 3: Dynamic Programming
class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        mem = [-1]*(n+1)
        mem[0] = 0
        for num in range(1, n+1):
            rem = num % 10
            if rem == 3 or rem == 4 or rem == 7:
                flag = -1
            elif rem == 2 or rem == 5 or rem == 6 or rem == 9:
                flag = 1
            else:
                flag = 0
            
            prev = num//10
            if mem[prev] == -1 or flag == -1:
                mem[num] = -1
            elif mem[prev] == 0 and flag == 0: 
                mem[num] = 0
            else:
                mem[num] = 1
                ans += 1
        return ans

# Time Complexity: O(n) 
# Space Complexity: O(n) 