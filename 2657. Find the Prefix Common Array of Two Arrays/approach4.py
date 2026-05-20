from typing import List

# Approach 4: Using a Frequency Array and a Counter
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        freq = [0]*(len(A)+1)
        count = 0
        for i in range(len(A)):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                count += 1
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                count += 1
            ans.append(count)
        return ans


# Time Complexity: O(n) where n is the length of the input arrays A and B.
# Space Complexity: O(n) for the frequency array used to count the occurrences of elements in A and B.