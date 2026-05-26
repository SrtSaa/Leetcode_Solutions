from typing import List

# Solution 2: Dynamic Programming
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        val = []
        for i in range(n):
            val.append((arr[i], i))
        val.sort(key= lambda x: x[0])

        ans = 0
        steps = [1]*n

        for item in val:
            idx = item[1]
            left, right = 0, 0
            for i in range(idx+1, min(n, idx+d+1)):
                if arr[i] >= arr[idx]:
                    break
                left = max(left, steps[i])
            for i in range(idx-1, max(-1, idx-d-1), -1):
                if arr[i] >= arr[idx]:
                    break
                right = max(right, steps[i])
            steps[idx] = max(left, right) + 1
            ans = max(ans, steps[idx])
        
        return ans
        

# Time complexity: O(n*log(n) + n*d) in the worst case, where n is the length of the input array and d is the maximum jump distance. The O(n*log(n)) comes from sorting the array, and O(n*d) comes from the nested loops that check for possible jumps for each index.
# Space complexity: O(n) for the steps array and the val array used for sorting.