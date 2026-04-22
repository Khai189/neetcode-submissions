class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        left = 1
        right = max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / mid)
            if totalTime <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
                