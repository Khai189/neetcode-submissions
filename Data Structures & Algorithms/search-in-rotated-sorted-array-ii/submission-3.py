class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # Rotated array
        # 11 11 11 11 12 2 4 4 5 5 6 6 8, target = 9
        # Mid is 4, so therefore since nums[right] >= nums[mid], that part is fully sorted but the number is not within there so we reset
        # Now its 11, however target isnt there

        
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True
            
            elif nums[left] == nums[mid] == nums[right]:
                left+=1
                right-=1
            
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1        

        return False