class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def turn(r,s):
            if r < 0 or r >=m or s<0 or s>=n or grid[r][s] == "0":
                return
            grid[r][s] = "0"
            turn(r-1,s)
            turn(r+1,s)
            turn(r,s-1)
            turn(r,s+1)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count+=1
                    turn(i,j)
        return count