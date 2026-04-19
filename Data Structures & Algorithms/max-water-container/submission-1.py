class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        window = 0
        while left < right:
            currentWindow = (right - left) * min(heights[left], heights[right])
            window = max(currentWindow, window)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
            
        return window
