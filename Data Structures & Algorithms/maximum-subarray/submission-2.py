class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = float("-inf")
        cur_sub = 0

        for num in nums:
            cur_sub += num
            max_sub = max(max_sub, cur_sub)
            if cur_sub < 0:
                cur_sub = 0
        
        return max_sub