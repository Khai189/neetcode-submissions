# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # first intuition, we can use a min-heap to keep track of the smallest integers and remove from it as we keep goin
        # however, this results in. O(n log k) time and O(n) space, and we can do better than that
        # we can use the intuition that bfs wil always result in a sorted array
        # we keep track of a res array with the elements, and we simply return the indexed bfs array 
        self.count = 0
        self.result = None
        def in_order(node):
            if not node or self.result is not None:
                return
            
            in_order(node.left)

            self.count+=1
            if self.count == k:
                self.result = node.val
                return
            
            in_order(node.right)
        
        in_order(root)
        return self.result