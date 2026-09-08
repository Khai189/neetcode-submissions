class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        
        max_freq = max(count.values())
        
        max_chunks = max_freq - 1
        empty_slots = max_chunks * n
        
        sorted_counts = sorted(count.values(), reverse=True)
        for freq in sorted_counts[1:]:
            empty_slots -= min(max_chunks, freq)
            
        idle_time = max(0, empty_slots)
        
        return len(tasks) + idle_time

