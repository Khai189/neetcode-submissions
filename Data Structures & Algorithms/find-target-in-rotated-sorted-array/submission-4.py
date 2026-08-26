class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        # 8 9, 0, 1, 3, 7 target = 5
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[right] >= nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                
                else:
                    right = mid - 1
            
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                
                else:
                    left = mid + 1


        return -1