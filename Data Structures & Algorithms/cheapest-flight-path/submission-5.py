class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # n airports 0 -> n-1 -> edges flights[i] = [from, to, weight/price], k -> max flights
        # find shortest paths
        # keep track -> (currentPrice, path 0->1: 1, 1-> 2 -> 2: )
        # BFS -> adjList = [0->1, 100], [0->2, 200], 1->3, 2->4, 3-> 4
        # path+1
        # currentPrice
        # So we want to implement a BFS 
        res = float("inf")
        queue = deque([(src, 0, -1)])
        adjList = [[] for _ in range(n)]
        for s, d, price in flights:
            adjList[s].append([d, price])

        prices = [float("inf")] * n
        while queue:
            node, cost, path = queue.popleft()

            if path <= k and node == dst:
                res = min(res, cost)
                continue

            if prices[node] > cost and path < k:
                prices[node] = cost
                for nei, weight in adjList[node]:
                    queue.append((nei, cost+weight, path+1))


        return res if res != float("inf") else -1