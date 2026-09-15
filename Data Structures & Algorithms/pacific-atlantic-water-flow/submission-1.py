class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        oceans_visited = set()

        queue = deque()

        for r in range(ROWS):
            queue.append((r, 0, True))
            queue.append((r, COLS-1, False))

        for c in range(COLS):
            queue.append((0, c, True))
            queue.append((ROWS-1, c, False))

        while queue:
            row, col, pacific = queue.popleft()
            state = (row, col, pacific)

            if state in oceans_visited:
                continue

            oceans_visited.add(state)

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and heights[nr][nc] >= heights[row][col]
                    and (nr, nc, pacific) not in oceans_visited
                ):
                    queue.append((nr, nc, pacific))

        output = []

        for r in range(ROWS):
            for c in range(COLS):
                reaches_pacific = (r, c, True) in oceans_visited
                reaches_atlantic = (r, c, False) in oceans_visited

                if reaches_pacific and reaches_atlantic:
                    output.append([r, c])

        return output
                    
        
            

        
            




    