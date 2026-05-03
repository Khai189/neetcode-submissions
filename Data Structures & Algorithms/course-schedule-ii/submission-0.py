class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we need to use topological sort and treat the prereqs as a graph with each list being an edge
        # we then construct the adj list and will do a topoligical sort using indegrees
        res = []
        indegrees = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegrees[n] == 0:
                q.append(n)

        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegrees[nei]-=1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == numCourses else []




            
