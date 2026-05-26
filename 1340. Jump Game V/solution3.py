from typing import List

# Solution 3: Monotonic Stack + DFS + Memoization
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        
        st = []
        prevGreater = [-1]*n
        for i in range(n):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            if st:
                prevGreater[i] = st[-1]
            st.append(i)
        
        st = []
        nextGreater = [-1]*n
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            if st:
                nextGreater[i] = st[-1]
            st.append(i)
        
        dp = [0]*n
        def solve(idx):
            if dp[idx] != 0:
                return dp[idx]
            
            left, right = 0, 0
            if prevGreater[idx] != -1 and idx - prevGreater[idx] <= d:
                left = solve(prevGreater[idx])
            if nextGreater[idx] != -1 and nextGreater[idx] - idx <= d:
                right = solve(nextGreater[idx])
            
            dp[idx] = max(left, right) + 1
            return dp[idx]
        
        ans = 0
        for i in range(n):
            ans = max(ans, solve(i))
        return ans


# Time complexity: O(n) for building the monotonic stacks and O(n) for the DFS with memoization, resulting in an overall time complexity of O(n).
# Space complexity: O(n) for the monotonic stacks, the prevGreater and nextGreater arrays, and the dp array used for memoization.