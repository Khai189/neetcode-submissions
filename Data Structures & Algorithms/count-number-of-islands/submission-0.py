class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # inherent idea, we perform a dfs in all directions
        # to save space, rather than adding a set to visit all areas, we replace old 1s with 0s
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        islands = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands +=1

        return islands
                

