class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        gas = nums[0]
        for num in nums[1:]:
            print(num, gas)
            if gas <= 0:
                return False
            gas = max(num, gas-1)
        
        return True