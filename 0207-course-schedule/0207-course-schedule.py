from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for pr in prerequisites:
            graph[pr[0]].append(pr[1])
        
        traced = set()
        visited = set()

        def dfs(v):
            if v in visited:
                return True
            if v in traced:
                return False
            traced.add(v)
            for w in graph[v]:
                if not dfs(w):
                    return False
            traced.remove(v)
            visited.add(v)
            return True
        for pr in prerequisites:
            if pr[0] not in visited:
                if not dfs(pr[0]):
                    return False
            if pr[1] not in visited:
                if not dfs(pr[1]):
                    return False
        
        return True