class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        q = deque()
        q.append((0, None))

        while q:
            node, parent = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei != parent:
                    q.append((nei, node))

        return len(visited) == n
        
            
