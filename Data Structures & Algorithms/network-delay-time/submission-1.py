class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # DAG, directed acylic graph
        # DAG shortest paths, 
        # Can we have 1,
        # 1, 2 -> shortest path, 1->4 shortest path, distrikas algorithim
        # [1: dist INFINITY, 2 INF, 3 INF]
        # minHeap, [2: 1, 4: 4]
        # [3: 1, 4: 4]
        # [4: 1]

        edges = collections.defaultdict(list)
        visit = set()
        for src, dst, t in times: 
            edges[src].append((dst, t))
        
        minHeap = [(0, k)]
        t = 0
        while minHeap:
            time, dst = heapq.heappop(minHeap)
            if dst in visit:
                continue
            visit.add(dst)
            t = time

            for dst2, time2 in edges[dst]:
                if dst2 not in visit:
                    heapq.heappush(minHeap, (time+time2, dst2))

        return t if len(visit) == n else -1