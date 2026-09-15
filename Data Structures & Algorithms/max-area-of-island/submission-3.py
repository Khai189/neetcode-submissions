class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue

                stack = [(r, c)]
                grid[r][c] = 0
                area = 0

                while stack:
                    cr, cc = stack.pop()
                    area += 1

                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc

                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 1
                        ):
                            grid[nr][nc] = 0
                            stack.append((nr, nc))

                max_area = max(max_area, area)

        return max_area


