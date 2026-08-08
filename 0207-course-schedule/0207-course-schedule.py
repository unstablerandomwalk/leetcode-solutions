class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1 or not prerequisites:
            return True
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[c].append(p)
            state = [0] * numCourses
        def has_cycle(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            state[node] = 1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True      
            state[node] = 2
            return False
        for i in range(numCourses):
            if has_cycle(i):
                return False
        
        return True