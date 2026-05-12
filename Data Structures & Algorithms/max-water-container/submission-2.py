class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Sliding window problem 
        l, r = 0, len(heights)-1
        window = 0
        while l <= r:
            product = min(heights[l], heights[r]) * (r-l)
            window = max(product, window)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return window            