class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
    
        queue = deque([(amount, 0)])
        visited = {amount} 
        
        while queue:
            curr_amt, count = queue.popleft()
            
            for coin in coins:
                next_amt = curr_amt - coin
                
                if next_amt == 0:
                    return count + 1 # Found the shortest path!
                
                if next_amt > 0 and next_amt not in visited:
                    visited.add(next_amt)
                    queue.append((next_amt, count + 1))
                    
        return -1

       