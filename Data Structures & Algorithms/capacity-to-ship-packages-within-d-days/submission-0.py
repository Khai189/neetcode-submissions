class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        ans = right

        def check_valid(target_num):

            spent_days = 1
            cur_day = 0

            for weight in weights:
                cur_day += weight

                if cur_day > target_num:
                    spent_days+=1
                    cur_day = weight
            
            return spent_days <= days
        
        while left <= right:
            mid = left + (right - left) // 2

            res = check_valid(mid)

            if res:
                ans = mid
                right = mid - 1
            
            else:
                left = mid + 1
        
        return ans


            