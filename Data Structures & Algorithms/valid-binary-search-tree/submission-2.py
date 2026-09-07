# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(low, high, root):
            if not root:
                return True
            
            if root.val <= low or root.val >= high:
                return False
            
            left = dfs(low, root.val, root.left)
            right = dfs(root.val, high, root.right)

            return left and right
        
        return dfs(float("-inf"), float("inf"), root)