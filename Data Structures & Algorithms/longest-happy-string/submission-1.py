import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        output = []

        max_heap = []
        
        if a:
            heapq.heappush(max_heap, (-a, "a"))
        
        if b:
            heapq.heappush(max_heap, (-b, "b"))
        
        if c:
            heapq.heappush(max_heap, (-c, "c"))

        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(output) >=2 and output[-1] == output[-2] == char:
                if max_heap:
                    second_count, second_char = heapq.heappop(max_heap)
                    output.append(second_char)
                    second_count +=1

                    if second_count < 0:
                        heapq.heappush(max_heap, (second_count, second_char))
                    
                    heapq.heappush(max_heap, (count, char))
                else:
                    return "".join(output)
            
            else:
                output.append(char)
                count+=1

                if count < 0:
                    heapq.heappush(max_heap, (count, char))
        
        return "".join(output)
                    

