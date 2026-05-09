class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        def simple_rob(start, end):
            r1, r2 = 0, 0
            for i in range(start, end):
                h = nums[i]
                temp = max(h + r1, r2)
                r1 = r2
                r2 = temp
            return r2

        return max(simple_rob(0, n - 1), simple_rob(1, n))