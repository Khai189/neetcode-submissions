class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            summedNum = numbers[left] + numbers[right]
            if summedNum < target:
                left+=1
            elif summedNum > target:
                right-=1
            else:
                return [left+1, right+1]