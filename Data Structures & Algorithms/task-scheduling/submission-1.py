import heapq
from collections import Counter
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_mp = Counter(tasks)
        maxHeap = [cnt for cnt in count_mp.values()]
        heapq.heapify_max(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:

            time+=1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = heapq.heappop_max(maxHeap)-1
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])
        return time
