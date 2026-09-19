class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        min_heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()

        while min_heap:
            water_level, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue
            
            visited.add((r, c))
            if r == ROWS-1 and c == COLS-1:
                return water_level
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    new_level = max(water_level, grid[nr][nc])
                    heapq.heappush(min_heap, (new_level, nr, nc))

        
        return -1