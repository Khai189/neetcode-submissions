# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, og, sub):
        if not og and not sub:
            return True
        if not (og and sub):
            return False
        if og.val != sub.val:
            return False
        return self.isSameTree(og.left, sub.left) and self.isSameTree(og.right, sub.right)
