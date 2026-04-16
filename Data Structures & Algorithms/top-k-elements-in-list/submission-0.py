import collections
from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = [(cnt, num) for num, cnt in counts.items()]
        heapq.heapify_max(heap)
        res = []
        for _ in range(k):
            _, num = heapq.heappop_max(heap)
            res.append(num)
        return res
         


            
        