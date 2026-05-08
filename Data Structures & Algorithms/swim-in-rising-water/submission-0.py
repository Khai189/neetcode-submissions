class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # We have a list lists = [
        # [0, 2, 1, 7] [16, 3, 4, 9], [15, 6, 8, 11], [19, 18, 23, 12]
        # ] 
        # DFS, end n-1, n-1, multi-source BFS 
        # BFS starting from 6
        # (n-1, n-1, highestWater)
        # Dijistrikas algorithimn
        # Min-heap to keep track of our current edge and water level 
        # total height
        # shortest paths + (highestPath)
        # visit = set()
        # dir = down, right
        # minHeap [totalHeight, (n, k)]
        # E log V 
        # O(V)
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        visited = set([(0, 0)])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while minHeap:
            max_h, r, c = heapq.heappop(minHeap)
            
            if r == N - 1 and c == N - 1:
                return max_h
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_max = max(max_h, grid[nr][nc])
                    heapq.heappush(minHeap, [new_max, nr, nc])
