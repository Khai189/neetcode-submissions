class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        
        val = -heapq.heappushpop(self.max_heap, -num)
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > len(self.max_heap):
            moved = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -moved)
            


    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        
        