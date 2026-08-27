class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # We want to split this up into several different problems
        # We want to ask ourselves whats the smallest total num we can have of contigous sub arrays such that k stays valid
        # Wait cant we just use binary search on the search space

        left, right = max(nums), sum(nums)

        def check_valid(sub_sum):
            sub_arrs = 1
            cur_sub = 0
            for num in nums:
                cur_sub += num
                if cur_sub > sub_sum:
                    sub_arrs +=1
                    if sub_arrs > k:
                        return False
                    cur_sub = num
            
            return sub_arrs <= k

        ans = right
        while left <= right:
            mid = left + (right - left) // 2

            if check_valid(mid):
                ans = mid
                right = mid - 1
            
            else:
                left = mid + 1
        
        return ans


