class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.helper(grid, i, j)
                    num_islands += 1
        return num_islands
                    
    def helper(self, grid, i, j):
        if i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] != '1' or i < 0 or j < 0:
            return 
        grid[i][j] = '2'
        self.helper(grid, i-1, j)
        self.helper(grid, i+1, j)
        self.helper(grid, i, j-1)
        self.helper(grid, i, j+1)   
        