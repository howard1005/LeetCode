class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        ans = 0

        ed = defaultdict(list)
        for i,(a,b) in enumerate(edges):
            ed[a].append(b)
            ed[b].append(a)
        
        def bfs(node):
            ret = None
            vis = set([node])
            dq = deque([(node,0)])
            while dq:
                node,c = dq.popleft()
                # print('bfs',node,c)
                ret = (node,c)
                for nnode in ed[node]:
                    if nnode in vis:
                        continue
                    vis.add(nnode)
                    dq.append((nnode,c+1))
            return ret,vis

        ddia = {}
        for node in range(1,n+1):
            if node in ddia:
                continue
            (_,c),vis= bfs(node)
            mx = 0
            for nn in vis:
                (_,c),_= bfs(nn)
                mx = max(mx,c)
            for nn in vis:
                ddia[nn] = mx
        # print(ddia)

        def diameter(node):
            # end_node,_ = bfs(node)
            # _,size = bfs(end_node)
            return ddia[node]+1

        gvis = defaultdict(int)

        def proc(node):
            gvis[node] = 0
            dq = deque([(node,0)])
            while dq:
                node,c = dq.popleft()
                for nnode in ed[node]:
                    if nnode in gvis:
                        if (gvis[nnode]&1) != (c+1)&1:
                            return -1
                        continue
                    gvis[nnode] = c+1
                    dq.append((nnode,c+1))
            return diameter(node)

        for node in range(1,n+1):
            # print('dia',diameter(node))
            if node in gvis:
                continue
            size = proc(node)
            # print('size',size)
            if size == -1:
                return -1
            ans += size

        return ans