class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rs = len(grid)
        cs = len(grid[0])
        island = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rs or c >= cs or grid[r][c]=="0":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(rs):
            for c in range(cs):
                if grid[r][c]== "1":
                    island += 1
                    dfs(r, c)
        return island
        