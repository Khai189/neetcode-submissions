# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # intuition, we need to keep track of previous max node
        # we set up dfs with a "max" that we keep track of with prev=max(prev, node.val)
        # if we see a new max, we add to the res the number of "good" nodes, else we keep going with previous max
        res = 0
        def dfs(root, currentMax):
            nonlocal res

            if not root:
                return
            if root.val >= currentMax:
                currentMax = root.val
                res+=1

            dfs(root.left, currentMax)
            dfs(root.right, currentMax)
        
        dfs(root, float("-infinity"))

        return res
