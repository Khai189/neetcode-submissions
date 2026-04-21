class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        stack = []
        # 7, 2, 3, 4, 1, 5, 6, 0, 4 7 9 0
        # 7, 4, 6, 8, 1, 10, 0, 4, 8, 12
        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                area = max(area, height * width)
            stack.append(i)
        return area