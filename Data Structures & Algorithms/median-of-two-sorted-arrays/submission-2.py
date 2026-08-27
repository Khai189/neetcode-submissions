class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        l, r = 0, m-1
        while True: 
            i = (l + r) // 2
            j = half - i - 2

            left_1 = nums1[i] if i >= 0 else float("-infinity")
            right_1 = nums1[i+1] if i < m - 1 else float("infinity")
            left_2 = nums2[j] if j >= 0 else float("-infinity")
            right_2 = nums2[j+1] if j < n - 1 else float("infinity")

            
            if left_1 <= right_2 and left_2 <= right_1:
                if total % 2 == 1:
                    return min(right_1, right_2)
                else:
                    return (max(left_1, left_2) + min(right_1, right_2)) / 2
                

            elif left_1 > right_2:
                r = i - 1
            
            else:
                l = i + 1


            