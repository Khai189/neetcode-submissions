class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difMap = {}
        for idx, num in enumerate(nums):
            print(target-num)
            print(difMap)
            if num in difMap:
                return [difMap[num], idx]
            
            difMap[target-num] = idx
        
        return []