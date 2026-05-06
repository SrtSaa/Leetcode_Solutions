from typing import List

# approach 1: using extra space
def rotate1(matrix: List[List[int]]) -> None:
    
    # Get the dimensions of the matrix
    m, n = len(matrix), len(matrix[0])

    # Create a new matrix to store the rotated image
    rotated = [[0] * m for _ in range(n)]
    
    # Fill the rotated matrix
    for i in range(m):
        for j in range(n):
            rotated[j][m - 1 - i] = matrix[i][j]
    
    return rotated

# Time complexity: O(n^2)
# Space complexity: O(n^2)



# approach 2: first transpose the matrix, then reverse each row
def rotate2(matrix: List[List[int]]) -> None:
    
    # Get the dimensions of the matrix
    m, n = len(matrix), len(matrix[0])

    # Create a new matrix to store the rotated image
    rotated = [[0] * m for _ in range(n)]

    # Fill the rotated matrix
    for i in range(m):
        for j in range(n):
            rotated[j][i] = matrix[i][j]

    # Reverse each row of the rotated matrix
    for i in range(n):
        rotated[i].reverse()
    
    return rotated

# Time complexity: O(n^2 + n^2*log(n)) 
## n^2 due to the nested loops for transposing the matrix,
## n^2*log(n) due to the reverse() function

# Space complexity: O(n) 
## due to the reverse() function, which uses O(n) space in the worst case.



# approach 3: first reverse the matrix, then transpose it
def rotate3(matrix: List[List[int]]) -> None:
    
    # Get the dimensions of the matrix
    m, n = len(matrix), len(matrix[0])

    # Reverse the matrix
    matrix.reverse()

    # Create a new matrix to store the rotated image
    rotated = [[0] * m for _ in range(n)]

    # Transpose the matrix
    for i in range(m):
        for j in range(n):
            rotated[j][i] = matrix[i][j]

    return rotated

# Time complexity: O(n^2 + n^2*log(n))
## n^2 due to the nested loops for transposing the matrix,
## n^2*log(n) due to the reverse() function

# Space complexity: O(n) 
## due to the reverse() function, which uses O(n) space in the worst case.





l = [
    [5, 4, 1, 3, 2],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 1]
]
rotated = rotate3(l)
for row in rotated:
    print(row)
