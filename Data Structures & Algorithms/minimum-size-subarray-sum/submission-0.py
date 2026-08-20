class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        window = 0
        min_len = float("inf")

        for right in range(len(nums)):
            window += nums[right]

            while window >= target:
                min_len = min(min_len, right - left + 1)
                window -= nums[left]
                left+=1
        
        return min_len if min_len != float("inf") else 0