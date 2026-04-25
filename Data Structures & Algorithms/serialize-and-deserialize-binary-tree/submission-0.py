# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: 
            return "N"
        res = []
        def bfs(root):
            
            queue = deque([root])

            while queue:
                node = queue.popleft()
                if not node:
                    res.append("N")
                else:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
        bfs(root)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N":
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))

        queue = deque([root])
        
        i = 1
        while queue and i < len(nodes):
            parent = queue.popleft()

            if nodes[i] != "N":
                parent.left = TreeNode(int(nodes[i]))
                queue.append(parent.left)
            i+=1

            if nodes[i] != "N":
                parent.right = TreeNode(int(nodes[i]))
                queue.append(parent.right)
            i+=1
        
        return root
        





