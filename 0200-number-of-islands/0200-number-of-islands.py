class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        def sink(r,c):
            if r>=m or c>=n or grid[r][c] != "1" or r<0 or c<0:
                return
            grid[r][c] = 0
            sink(r+1,c)
            sink(r-1,c)
            sink(r,c+1)
            sink(r,c-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    sink(i,j)
                    count += 1
        return count