class Solution:
    def numIslands(self, grid):
        if grid == None or len(grid) == 0:
            return 0

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs( grid, row, col):
        
            if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0"):
                return       

            else:
                grid[row][col] = "0" # MARK the current element - so it is VISITED
                dfs(grid, row+1, col)
                dfs(grid, row, col+1)
                dfs(grid, row-1, col)
                dfs(grid, row, col-1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(grid, row, col)

        return islands
    
    