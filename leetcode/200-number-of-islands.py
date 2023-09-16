# DFS solution
# O(num_rows x num_cols) time and space
class Solution:
    def dfs(self, grid, row, col):
        num_rows = len(grid)
        num_cols = len(grid[0])
        grid[row][col] = '0'
        if row - 1 >= 0 and grid[row-1][col] == '1':
            self.dfs(grid, row - 1, col)
        if row + 1 < num_rows and grid[row+1][col] == '1':
            self.dfs(grid, row + 1, col)
        if col - 1 >= 0 and grid[row][col-1] == '1':
            self.dfs(grid, row, col - 1)
        if col + 1 < num_cols and grid[row][col+1] == '1':
            self.dfs(grid, row, col + 1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    num_islands += 1
                    self.dfs(grid, row, col)
        return num_islands