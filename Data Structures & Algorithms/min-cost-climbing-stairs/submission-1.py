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

        prev2, prev1 = cost[0], cost[1]

        for i in range(2, len(cost)):
            cur = min(prev2, prev1) + cost[i]
            prev2 = prev1
            prev1 = cur
        
        return min(prev2, prev1)