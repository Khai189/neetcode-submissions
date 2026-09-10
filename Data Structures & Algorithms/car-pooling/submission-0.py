class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])

        cur_passengers = 0
        min_heap = []
        for trip in trips:
            passengers, start, end = trip

            while min_heap and min_heap[0][0] <= start:
                _, prev_passengers = heapq.heappop(min_heap)
                cur_passengers-=prev_passengers
            
            cur_passengers+=passengers
            if cur_passengers > capacity:
                return False
            
            heapq.heappush(min_heap, (end, passengers))


        return True
