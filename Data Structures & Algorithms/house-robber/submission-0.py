class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2, 5, 8, 3, 1, 5]
        # [2, 5]
        # [1, 5, 2, 3, 21, 16]
        # -> 2, 3 -> 4
        # 0, 1?
        
        rob1, rob2 = 0, 0
        for n in nums:
            # Logic: What's better? 
            # Current house + two houses ago OR just the previous house's total?
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2