class UnionFind():

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def _find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self._find(self.parent[node])
        
        return self.parent[node]
    
    def _union(self, node1, node2):
        p1 = self._find(node1)
        p2 = self._find(node2)

        if p1 == p2:
            return False

        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1
        
        self.parent[p2] = p1
        self.size[p1] += self.size[p2]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # we need to find the connections for each node
        # DSU

        uf = UnionFind(n)
        components = n
        for u, v in edges:
            if uf._union(u, v):
                components-=1


        return components