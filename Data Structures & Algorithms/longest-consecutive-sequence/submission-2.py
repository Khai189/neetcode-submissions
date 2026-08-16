class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = set(nums)
        LCS = 0
        for num in nums:

            if num - 1 not in unique:
                length = 0
                while num + length in unique:
                    length+=1
                
                LCS = max(length, LCS)
        
        return LCS