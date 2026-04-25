import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []
        for x, y in points:
            distance = (x**2 + y**2)
            heapq.heappush_max(maxHeap, [distance, x, y])
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
            
        while maxHeap:
            dist, x, y = heapq.heappop_max(maxHeap)
            res.append([x, y])
        return res





