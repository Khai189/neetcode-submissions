class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = [False] * n
        adj = [[] for _ in range(n)]
        # Idea: what are the inputs, we have arrays representing the edges, 
        # Do we return 0 if the output is empty?
        # Can there be duplicates?
        # IMPORTANT: can there be a cycle??????
        # Thought process:
        # Perform a DFS solution by taking in elements and putting them in the visit set
        # Each time we add the new node to the visit set we then search further along
        # We stop whenever we hit no more edges
        # We just loop over the edges and we visit them incrementally 
        # Question: How do we keep track of connections?

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res+=1
        
        return res