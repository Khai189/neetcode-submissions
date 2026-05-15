class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} # Maps (r, c) -> longest increasing path starting at (r, c)
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # 1. If we already calculated the answer for this cell, return it instantly
            if (r, c) in dp:
                return dp[(r, c)]
            
            # Base case: every individual cell has a minimum path length of 1 (itself)
            max_path = 1
            
            # 2. Explore all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and ensure the neighbor is STRICTLY greater
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    # The path starting here is 1 (current cell) + whatever the neighbor can achieve
                    max_path = max(max_path, 1 + dfs(nr, nc))
            
            # 3. Cache the final answer for this cell before returning
            dp[(r, c)] = max_path
            return max_path

        # Run DFS from every single cell to find the global maximum
        global_max = 0
        for r in range(ROWS):
            for c in range(COLS):
                global_max = max(global_max, dfs(r, c))
                
        return global_max
