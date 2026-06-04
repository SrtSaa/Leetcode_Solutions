# Approach 1: Digit-based approach
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for num in range(max(100, num1), num2+1):
            post = num % 10
            num = num // 10
            while num >= 10:
                curr = num % 10
                num = num // 10
                prev = num % 10
                if (curr > prev and curr > post) or (curr < prev and curr < post):
                    ans += 1
                post = curr
        return ans



# Time Complexity: O(n * log(n)) where n is the number of integers in the range [num1, num2]
# Space Complexity: O(1)