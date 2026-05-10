class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Sliding window approach, where we move the left pointer each time
        # we hit a negative number and record the max of the prev window and
        # see if it's bigger than the previous.
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            tmp = curMax*n
            curMax = max(tmp, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)

        return res