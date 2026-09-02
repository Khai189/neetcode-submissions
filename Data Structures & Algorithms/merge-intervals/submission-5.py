class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        prev_start, prev_end = intervals[0]
        output = [[prev_start, prev_end]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if prev_end < start:
                output.append([start, end])
                prev_start, prev_end = start, end
            
            else:
                output[-1][1] = max(end, prev_end)
                prev_end = max(end, prev_end)
            
            
        
        return output
