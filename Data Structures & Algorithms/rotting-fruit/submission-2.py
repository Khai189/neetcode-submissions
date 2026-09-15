class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # what are the inputs?
        # We have a grid with three possible variables
        # 0, empty which we cannot traverse
        # 1, fresh fruit, can be traveresed
        # 2, rotten fruit, source of traversal
        # The question is asking us: how long until there are zero fresh fruits remaining?
        # This outcome is not guaranteed however, and if we cannot achieve it we must return -1
        # So from the beginning we have to ask ourselves, how do we track how many fruits become rotten in a sinfgle interval of time
        # There's this method called peeling an onion which is basically a multi source BFS where we start with every single rotten fruit
        # We then process everything in the queue level by level, incrementing time for each level we process 
        # We then keep going until we've processed all possible neighbors via our BFS solution
        # We then check to see if the total number of rotten fruits, which will be represented with a counter, is equal to the total number of all fruits in the beginning, which we will process with an initial queue fill 

        ROWS, COLS = len(grid), len(grid[0])
        fresh_fruit = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                # fresh fruit
                if grid[r][c] == 1:
                    fresh_fruit+=1
                
                # rotten fruit
                elif grid[r][c] == 2:
                    queue.append((r, c))
        

        if fresh_fruit == 0:
            return 0

        time = 0
        while fresh_fruit > 0 and queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        fresh_fruit-=1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            
            time+=1
        
        return time if fresh_fruit == 0 else -1














