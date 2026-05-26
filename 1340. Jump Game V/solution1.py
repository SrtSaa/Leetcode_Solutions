from typing import List

# Solution 1: DFS + Memoization
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        steps = [0]*n
        def dfs(idx):
            if steps[idx] != 0:
                return steps[idx]
            
            left, right = 0, 0
            for i in range(idx-1, max(-1, idx-d-1), -1):
                if arr[i] >= arr[idx]:
                    break
                left = max(left, dfs(i))
            for i in range(idx+1, min(n, idx+d+1)):
                if arr[i] >= arr[idx]:
                    break
                right = max(right, dfs(i))
            steps[idx] = max(left, right) + 1

            return steps[idx]
    

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        
        return ans
        

# Time complexity: O(n*d) in the worst case, where n is the length of the input array and d is the maximum jump distance. This is because in the worst case, we may need to explore all possible jumps for each index.  
# Space complexity: O(n) for the memoization array and the recursion stack in the worst case.