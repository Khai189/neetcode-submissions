# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root:
                return []
            res = []
            curr_level = 0
            q = deque([root])
            while q:
                len_q = len(q)
                res.append([])
                
                for _ in range(len_q):
                    node = q.popleft()
                    res[curr_level].append(node.val)

                    if node.left:
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)
                
                curr_level+=1
            return res
            
        return bfs(root)


