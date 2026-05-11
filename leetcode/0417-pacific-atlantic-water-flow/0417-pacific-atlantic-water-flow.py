class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visit):

            visit.add((r, c))

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Check boundaries
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue

                # Already visited
                if (nr, nc) in visit:
                    continue

                # Can only move to equal/higher height
                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, visit)

        # Pacific borders
        for c in range(COLS):
            dfs(0, c, pacific)          # top row
            dfs(ROWS - 1, c, atlantic) # bottom row

        for r in range(ROWS):
            dfs(r, 0, pacific)         # left column
            dfs(r, COLS - 1, atlantic) # right column

        # Cells reachable by both
        result = []

        for r in range(ROWS):
            for c in range(COLS):

                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
    