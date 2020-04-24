class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] =='1':
                    islands+=1
                    self.set_island(i,j,grid)
        return islands
    def set_island(self,i,j,grid):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
            return 
        if grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.set_island(i+1,j,grid)
        self.set_island(i-1,j,grid)
        self.set_island(i,j+1,grid)
        self.set_island(i,j-1,grid)
