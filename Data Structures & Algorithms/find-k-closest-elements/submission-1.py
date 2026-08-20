class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        


        left, right = 0, len(arr)-k
        while left < right:
            mid = left + (right - left) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            
            else:
                right = mid
        
        return arr[right : right + k]



