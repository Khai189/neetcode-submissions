class UnionFind():

    def __init__(self, n):
        self.comps = n
        self.parents = [i for i in range(n+1)]
        self.size = [1] * (n+1)

    
    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False

        self.comps -= 1
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parents[pv] = pu
        return True

    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n - 1:
            return False

        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return False
        return uf.components() == 1
        
