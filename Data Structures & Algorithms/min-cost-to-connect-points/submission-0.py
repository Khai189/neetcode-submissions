class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # x, y co-ordinate point [x, y] x, y
        # [x, y] -> -5, -5
        # [[0, 5]] -> 0
        # Minimum Spanning Tree
        # Prims and Kruskals
        # Graph points -> edges 
        # Kruskals 
        # [[0, 5], [1, 5], [3, 6], [5, 7], [2, 5]]
        # 1, 3, 3
        # 7
        # Prims [[0, 5]]
        # adjacency List, [0, 5] -> 1, 4, 12
        # [1, 5], [1, 5] -> 3, 6
        # [3, 6] -> 3
        # 5, 7
        # min heap edges

        n, node = len(points), 0
        dist = [10000000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n-1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curDist = (abs(points[i][0] - points[node][0]) +
                           abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            
            res += dist[nextNode]
            node = nextNode
            edges+=1
        
        return res