class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return list(range(n))
        adj_list = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

            indegree[u]+=1
            indegree[v]+=1


        queue = deque(i for i in range(n) if indegree[i] == 1)

        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(queue)
            remaining_nodes -= leaves_count

            for _ in range(leaves_count):
                leaf = queue.popleft()
                for neighbor in adj_list[leaf]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)
