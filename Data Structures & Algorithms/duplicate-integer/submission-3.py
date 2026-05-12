class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        visited = set(nums)

        return len(visited) != len(nums)