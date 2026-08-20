class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        write = 1
        for read in range(len(nums)):
            if read > 0 and nums[read] != nums[read-1]:
                nums[write] = nums[read]
                write+=1
        
        return write