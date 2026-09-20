class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        window = 0
        min_size = float("inf")
        for right in range(len(nums)):
            window += nums[right]

            while window >= target:
                min_size = min(min_size, right - left + 1)
                window-=nums[left]
                left+=1
            
        
        return min_size if min_size != float("inf") else 0