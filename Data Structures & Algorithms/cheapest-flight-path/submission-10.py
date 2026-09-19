class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append((v, cost))

        min_heap = [(0, src, 0)]
        min_stops = [float('inf')] * n

        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)

            if node == dst:
                return cost

            if stops >= min_stops[node] or stops > k:
                continue

            min_stops[node] = stops

            for nei, price in adj[node]:
                heapq.heappush(min_heap, (cost + price, nei, stops + 1))

        return -1



            






