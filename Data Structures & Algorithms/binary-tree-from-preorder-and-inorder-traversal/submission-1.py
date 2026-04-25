# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #      0
        #   4     5
        #3    7 2   8, preorder = 0, 4, 3, 7, 5, 2, 8, inorder = 3, 4, 7, 0, 2, 5, 8
        in_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def arrayToTree(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx+=1

            mid = in_map[root.val]
            root.left = arrayToTree(left, mid-1)
            root.right = arrayToTree(mid+1, right)

            return root
        
        return arrayToTree(0,len(preorder)-1)

