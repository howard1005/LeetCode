class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        ans = 1

        cum = sum(values)
        if cum % k != 0:
            return ans
        
        d = defaultdict(set)
        for a,b in edges:
            d[a].add(b)
            d[b].add(a)

        def dfs(node,par):
            nonlocal ans
            vl = [values[node]]
            for nnode in d[node]:
                if nnode == par:
                    continue
                v = dfs(nnode,node) 
                if v % k == 0:
                    ans += 1
                vl.append(v)
            # print(node,vl)
            return sum(vl)

        dfs(0,-1)
        
        return ans