class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2

            val = nums[mid]

            if val == target:
                return mid 
            
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                
                else:
                    right = mid - 1
        
        return -1 


# Input: nums = [3,4,5,6,1,2], target = 1
# Output: 4
# An array of integers -> int, and that int represents the index of the target element if found, else -1
# The array itself WAS sorted, before it was randomly shifted by n times, of which we don't know N
# [1, 2, 5, 8, 19, 23] -> 19, this gets rooted to [19, 21, 1, 2, 5, 8]
# left, right = 0, 5 -> 2, 21
# nums[left] -> nums[mid] contain the number?
# if nums[left] <= target < nums[mid] -> right = mid - 1
# left = mid + 1
# nums[mid] -> nums[right]
#  1 2 5 8, target in between nums[mid] and nums[right], 
# right = mid -1 

