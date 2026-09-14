class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        used = [False] * len(nums)

        def backtrack(k_remaining: int, cur_sum: int, start: int) -> bool:
            if k_remaining == 1:
                return True

            # Current bucket is complete; start the next bucket from index 0
            if cur_sum == target:
                return backtrack(k_remaining - 1, 0, 0)

            for i in range(start, len(nums)):
                if used[i] or cur_sum + nums[i] > target:
                    continue

                if i > start and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                if backtrack(k_remaining, cur_sum + nums[i], i + 1):
                    return True
                used[i] = False

                if cur_sum == 0:
                    break

            return False

        return backtrack(k, 0, 0)