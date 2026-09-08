class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for x, y in points:
            dist = (x**2 + y**2) ** 0.5
            heapq.heappush(heap, (-dist, (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)
        
        output = []
        while len(heap) > 0:
            _, coordinates = heapq.heappop(heap)
            x, y = coordinates
            output.append([x, y])
        
        return output