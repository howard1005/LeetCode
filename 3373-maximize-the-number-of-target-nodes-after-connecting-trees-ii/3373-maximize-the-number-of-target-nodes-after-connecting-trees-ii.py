class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        ans = []

        n = len(edges1)+1
        m = len(edges2)+1
        
        ed1 = defaultdict(set)
        for a,b in edges1:
            ed1[a].add(b)
            ed1[b].add(a)

        ed2 = defaultdict(set)
        for a,b in edges2:
            ed2[a].add(b)
            ed2[b].add(a)

        d1 = defaultdict(lambda:-1)
        d2 = defaultdict(lambda:-1)

        def bfs(d,ed):
            vis = set()
            dq = deque()
            vis.add(0)
            dq.append((0,0))

            while dq:
                node,c = dq.popleft()
                d[node] = c
                for nn in ed[node]:
                    if nn in vis:
                        continue
                    vis.add(nn)
                    dq.append((nn,c^1))

        bfs(d1,ed1)
        bfs(d2,ed2)

        rd1 = defaultdict(set)
        rd2 = defaultdict(set)

        for k,c in d1.items():
            rd1[c].add(k)

        for k,c in d2.items():
            rd2[c].add(k)

        mx = max(len(rd2[0]),len(rd2[1]))

        for i in range(n):
            c = d1[i]
            ans.append(len(rd1[c])+mx)

        return ans