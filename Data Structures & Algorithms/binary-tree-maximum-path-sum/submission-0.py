# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-infinity")
        def dfs(root):
            if not root:
                return 0
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            self.max_sum = max(self.max_sum, root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return self.max_sum 