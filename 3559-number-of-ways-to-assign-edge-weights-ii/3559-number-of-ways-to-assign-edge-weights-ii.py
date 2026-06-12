class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []

        MOD = 1000000007

        ed = defaultdict(set)
        for a,b in edges:
            ed[a].add(b)
            ed[b].add(a)

        n = len(edges)+1

        vis = {1:0}
        dq = deque([(1,0,-1)])
        nl = [[] for _ in range(n+1)]
        while dq:
            i,dep,pi = dq.popleft()
            if pi != -1:
                l = nl[i]
                l.append(pi)
                j = 0
                while j < len(nl[l[j]]):
                    l.append(nl[l[j]][j])
                    j += 1
            for ni in ed[i]:
                if ni in vis:
                    continue
                vis[ni] = dep+1
                dq.append((ni,dep+1,i))

        # print(nl)

        for a,b in queries:
            if a == b:
                ans.append(0)
                continue
            if vis[a] > vis[b]:
                a,b = b,a
            adep,bdep = vis[a],vis[b]
            diff = bdep-adep
            for i in range(len(nl[b])-1,-1,-1):
                if (1<<i) <= diff:
                    diff -= (1<<i)
                    b = nl[b][i]
                if diff == 0:
                    break
            if a == b:
                ans.append(pow(2,bdep-adep-1,MOD))
                continue

            # print(f"a,b {a},{b},{vis[a]},{vis[b]},{nl[a]},{nl[b]}")
            
            for i in range(len(nl[a])-1,-1,-1):
                # print(f"i {i}, {a},{b},{vis[a]},{vis[b]},{nl[a]},{nl[b]}")
                if i < len(nl[a]) and nl[a][i] != nl[b][i]:
                    a,b = nl[a][i],nl[b][i]
            c = nl[a][0]
            cdep = vis[c]
            ans.append(pow(2,adep+bdep-2*cdep-1,MOD))

        return ans