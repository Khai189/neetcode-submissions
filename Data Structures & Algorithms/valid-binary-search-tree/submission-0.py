# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # intuition, use dfs and pass down the current root 
        # if right is less than or left is less than the roots value, we return false using an and statement on each return
        def dfs(root, low, high):
            if not root:
                return True
            
            if not low < root.val < high:
                return False
            
            return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
        
        return dfs(root, float("-infinity"), float("infinity"))
            

