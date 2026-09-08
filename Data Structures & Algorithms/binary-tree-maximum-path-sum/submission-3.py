# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_path = float("-inf")
        def dfs(root):
            if not root:
                return 0
            
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            max_possible_path = root.val + left + right
            self.max_path = max(max_possible_path, self.max_path)

            return root.val + max(left, right)

        dfs(root)

        return self.max_path