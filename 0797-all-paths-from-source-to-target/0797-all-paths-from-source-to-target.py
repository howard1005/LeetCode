class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(n,l):
            if n == len(graph)-1:
                nonlocal ans
                ans.append(l)
                return
            for nn in graph[n]:
                dfs(nn,l+[nn])
        dfs(0,[0])
        return ans