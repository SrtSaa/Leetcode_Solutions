class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        newGrid = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                newGrid[j][m - 1 - i] = box[i][j]

        for col in range(m):
            bottom = n-1
            for curr_pos in range(n-1, -1, -1):
                if newGrid[curr_pos][col] == ".":
                    continue
                elif newGrid[curr_pos][col] == "#":
                    newGrid[bottom][col] = "#"
                    if bottom != curr_pos:
                        newGrid[curr_pos][col] = "."
                    bottom -= 1
                elif newGrid[curr_pos][col] == "*":
                    bottom = curr_pos - 1

        return newGrid



# Time Complexity: O(m*n) 
# Space Complexity: O(m*n)