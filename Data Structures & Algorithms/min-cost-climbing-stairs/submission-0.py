class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [1, 3, 2]
        # [-1, 3, 0, -5]
        # [1 <- ] 1, 2
        # [1, 2, 4, 5, 0]
        # fibonnaci sequence 
        # DFS O(2^n)
        # DP: 1 -> 2 -> 4 -> 5 -> 0 -> 12 
        # DP: Cache: 1 -> 4, cache = {} <- O(n)

        cost.append(0)
    
        # 2. Iterate backwards from the third-to-last step to the start
        for i in range(len(cost) - 3, -1, -1):
            # The cost of step 'i' is its own cost PLUS 
            # the minimum of the next two steps
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        # 3. The answer is the min of starting at index 0 or index 1
        return min(cost[0], cost[1])