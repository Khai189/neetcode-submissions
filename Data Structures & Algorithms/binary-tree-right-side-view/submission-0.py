# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #        0
        #       4 5
        #     5     7
        #   6   7
        # {level: right, level1: right, level2: right}
        # level-order traversal, keep track of most rightward element, record it.
        res = []
        def dfs(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append(root.val)
            
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)
        
        dfs(root, 0)
        return res

            
        