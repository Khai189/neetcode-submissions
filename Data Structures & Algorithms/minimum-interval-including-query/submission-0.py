class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])

        heap = []
        ind = 0

        res = {}

        for query in sorted(queries):
            while ind < len(intervals) and intervals[ind][0] <= query:
                start, end = intervals[ind]
                heapq.heappush(heap, (end - start + 1, end))
                ind+=1    

            
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            res[query] = heap[0][0] if heap else -1
            
        return [res[q] for q in queries]
        

            

            

            

