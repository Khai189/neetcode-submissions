class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        curArr = 0
        lastArr = len(matrix)-1
        while curArr <= lastArr:
            midArr = (curArr + lastArr) // 2
            if matrix[midArr][-1] < target:
                curArr = midArr +1
            elif target < matrix[midArr][0]:
                lastArr = midArr - 1
            else:
                break
        
        if not (curArr <= lastArr):
            return False
        row = (curArr + lastArr) // 2
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False





