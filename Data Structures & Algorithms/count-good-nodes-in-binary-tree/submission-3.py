# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = 0


        def dfs(parent, node):
            nonlocal output
            if not node:
                return None
            
            if node.val >= parent:
                output +=1
                parent = node.val
            
            dfs(parent, node.right)
            dfs(parent, node.left)
        
        dfs(float("-inf"), root)
        return output