class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:  

        adj_list = defaultdict(list)
        for u, v, dist in times:
            adj_list[u].append((dist, v))
        
        min_heap = [(0, k)]
        visited = set()
        

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)

            if len(visited) == n:
                return dist

            for time, nei in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (dist + time, nei))



        return -1