from typing import List

# approach 1: using extra space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Get the dimensions of the matrix
        n = len(matrix)

        # Create a new matrix to store the rotated image
        temp = [[0]*n for _ in range(n)]

        # Fill the rotated matrix
        for i in range(n):
            for j in range(n):
                temp[j][n-1-i] = matrix[i][j]

        # Copy the rotated matrix back to the original matrix
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[i][j]

# time complexity: O(n^2)
# space complexity: O(n^2)