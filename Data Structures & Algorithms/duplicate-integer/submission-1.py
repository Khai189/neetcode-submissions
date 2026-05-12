class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num in count.keys():
                return True
            else:
                count[num] = 1
        
        return False