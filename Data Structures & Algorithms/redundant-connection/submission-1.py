class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # we need to look for cycles in a graph
        # edge cases
        # so, first off, I'm thinking about a graph and and adj list
        # graphs usually involve some type of search, BFS, DFS, Disjoint Set Union, etc
        # How do we actually find cycles in a graph?
        # Answer should be obvious, we have a destination already in our visited set
        # We need to keep track of visited nodes within the graph
        # Once we find a node thats been tracked, we need to have its edge be the current "latest" edge we've tracked
        # We can also use union find for this! by keeping track of parents we instantly find a cycle
        N = len(edges)
        par = [i for i in range(N+1)]
        rank = [1] * (N+1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] +=1
            else:
                par[p1] = p2
                rank[p2] +=1
            
            
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]



        
