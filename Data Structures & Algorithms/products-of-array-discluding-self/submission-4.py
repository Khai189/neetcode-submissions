class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prev = [1] * (len(nums))
        for i in range(1, len(nums)):
            prev[i] = nums[i-1] * prev[i-1]
        

        output = [0] * len(nums)

        suffix_count = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = (prev[i] * suffix_count)
            suffix_count*=nums[i]
        
        return output