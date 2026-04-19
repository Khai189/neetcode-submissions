class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mappedNums = set(nums)
        longest = 0
        for num in mappedNums:
            if num-1 not in mappedNums:
                length = 1
                while (num+length) in mappedNums:
                    length +=1
                longest = max(length, longest)
        return longest



