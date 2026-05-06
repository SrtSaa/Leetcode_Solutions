from typing import List

# approach 2: in-place, first transpose the matrix, then reverse each row
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

# Time complexity: O(n^2 + n^2*log(n)) 
## n^2 due to the nested loops for transposing the matrix, 
## n^2*log(n) due to the reverse() function

# Space complexity: O(n) 
## due to the reverse() function, which uses O(n) space in the worst case.


# approach 2: in-place, first reverse the matrix, then transpose it
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()

        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
# Time complexity: O(n^2 + n^2*log(n)) 
## n^2 due to the nested loops for transposing the matrix, 
## n^2*log(n) due to the reverse() function

# Space complexity: O(n) 
## due to the reverse() function, which uses O(n) space in the worst case.
        