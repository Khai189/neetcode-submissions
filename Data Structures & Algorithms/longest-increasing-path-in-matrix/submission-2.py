class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} 
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            
            max_path = 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(nr, nc))
            
            dp[(r, c)] = max_path
            return max_path

        global_max = 0
        for r in range(ROWS):
            for c in range(COLS):
                global_max = max(global_max, dfs(r, c))
                
        return global_max
