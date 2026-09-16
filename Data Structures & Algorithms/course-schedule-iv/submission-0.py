class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj_list = defaultdict(list)

        indegree = [0] * numCourses

        for pre_req, course in prerequisites:
            adj_list[pre_req].append(course)
            indegree[course]+=1
        
        queue = deque()
        for course in range(len(indegree)):
            if indegree[course] == 0:
                queue.append(course)
            
        pre_reqs = defaultdict(set)
        while queue:
            course = queue.popleft()

            for future_class in adj_list[course]:
                pre_reqs[future_class].add(course)
                pre_reqs[future_class] |= (pre_reqs[course])

                indegree[future_class] -= 1
                if indegree[future_class] == 0:
                    queue.append(future_class)

        return [u in pre_reqs[v] for u, v in queries]



       

        
