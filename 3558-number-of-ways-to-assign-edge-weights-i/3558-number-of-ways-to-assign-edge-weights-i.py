class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 1000000007

        ed = defaultdict(set)
        for a,b in edges:
            ed[a].add(b)
            ed[b].add(a)
        
        mxdep = 0
        vis = set([1])
        dq = deque([(1,0)])
        while dq:
            i,dep = dq.popleft()
            mxdep = max(mxdep,dep)
            for ni in ed[i]:
                if ni in vis:
                    continue
                vis.add(ni)
                dq.append((ni,dep+1))

        ans = pow(2,mxdep-1,MOD)

        return ans