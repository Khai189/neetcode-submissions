class UnionFind():

    def __init__(self, n):
        self.parents = list(range(n+1))
        self.rank = [1] * (n+1)
    
    def _find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self._find(self.parents[node])
        
        return self.parents[node]
    
    def _union(self, node1, node2):
        p1 = self._find(node1)
        p2 = self._find(node2)

        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        
        self.parents[p2] = p1
        self.rank[p1] += self.rank[p2]
        return True
    


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        uf = UnionFind(len(edges))
        redundant = [-1, -1]

        for u, v in edges:
            if not uf._union(u, v):
                redundant = [u, v]
        
        return redundant
