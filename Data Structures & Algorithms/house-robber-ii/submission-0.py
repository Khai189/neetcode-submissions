class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def simple_rob(houses):
            r1, r2 = 0, 0
            for house in houses:
                temp = max(house + r1, r2)
                r1 = r2
                r2 = temp
            return r2
        
        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))