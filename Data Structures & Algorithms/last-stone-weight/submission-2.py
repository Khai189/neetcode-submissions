import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 > stone2:
                heapq.heappush_max(stones, stone1-stone2)
            elif stone2 > stone2:
                heapq.heappush_max(stones, stone2-stone1)
            else:
                continue
        return stones[0] if stones else 0

