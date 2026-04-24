class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        perimeter = 0
        def dfs(r, c):
            nonlocal perimeter
            # build boundary
            if r<0 or c<0 or r >= rows or c >= cols or grid[r][c]== 0:
                perimeter +=1
                return 
            if (r, c) in visited:
                return
            visited.add((r, c))
            dfs(r, c-1)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r+1, c)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    dfs(r, c)
                    return perimeter
                    