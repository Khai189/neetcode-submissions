# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(parent, node):
            if not node:
                return 0
            
            res = 0
            if node.val >= parent:
                res +=1
                parent = node.val
            
            left = dfs(parent, node.right)
            right = dfs(parent, node.left)
            return res + left + right
        
        return dfs(float("-inf"), root)
