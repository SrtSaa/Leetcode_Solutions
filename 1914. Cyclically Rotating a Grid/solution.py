from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        def rotate(nums: List[int], k: int) -> None:
            def reverse(nums, start, end):
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1

            n = len(nums)
            k = k % n
            reverse(nums, 0, k-1)
            reverse(nums, k, n-1)
            reverse(nums, 0, n-1)
        
        m, n = len(grid), len(grid[0])

        row_start, row_end = 0, m-1
        col_start, col_end = 0, n-1
        while row_start < m//2 and col_start < n//2:
            layer = []

            # Get the elements of the current layer in clockwise order
            for i in range(col_start, col_end):
                layer.append(grid[row_start][i])
            for i in range(row_start, row_end):
                layer.append(grid[i][col_end])
            for i in range(col_end, col_start, -1):
                layer.append(grid[row_end][i])
            for i in range(row_end, row_start, -1):
                layer.append(grid[i][col_start])

            # Rotate the layer by k positions
            x = k % len(layer)
            rotate(layer, x)

            # Place the rotated elements back into the grid
            idx = 0
            for i in range(col_start, col_end):
                grid[row_start][i] = layer[idx]
                idx += 1
            for i in range(row_start, row_end):
                grid[i][col_end] = layer[idx]
                idx += 1
            for i in range(col_end, col_start, -1):
                grid[row_end][i] = layer[idx]
                idx += 1
            for i in range(row_end, row_start, -1):
                grid[i][col_start] = layer[idx]
                idx += 1
            row_start += 1
            col_start += 1
            row_end -= 1
            col_end -= 1


        return grid



# Time Complexity: O(m*n)
# Space Complexity: O(m+n)