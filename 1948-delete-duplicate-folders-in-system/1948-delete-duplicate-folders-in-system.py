class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        ans = []

        d = defaultdict(lambda:-1)
        cd = {}

        for i,path in enumerate(paths):
            t = tuple(path)
            d[t] = i
            cd[i] = path[-1]

        # print(f"d : {d}, cd : {cd}")
        
        pd = {}
        ed = defaultdict(set)

        for i,path in enumerate(paths):
            t = tuple(path[:-1])
            idx = d[t]
            pd[i] = idx
            ed[idx].add(i)
            ed[i]

        # print(f"pd : {pd}, ed : {ed}")


        surfixd = defaultdict(set)
        rsurfixd = defaultdict(list)
        rsurfixd[-1]

        def rdfs(i,dq):
            # print(f"rdfs {i}, {dq}")
            if i == -1:
                return
            rsurfixd[i].append(tuple(dq))

            dq.appendleft(cd[i])
            
            pi = pd[i]
            t = tuple(dq)
            surfixd[t].add(pi)
            
            rdfs(pi,dq)

        for i,sd in ed.items():
            if not sd:
                rdfs(i,deque())

        # print(f"surfixd : {surfixd}")
        # print(f"rsurfixd : {rsurfixd}")

        deld = set()

        for idx,l in rsurfixd.items():
            if idx in deld or not l:
                continue
            sub = surfixd[l[0]].copy()
            for t in l[1:]:
                tsub = surfixd[t]
                sub &= tsub
            if len(sub)>=2:
                for ti in sub:
                    if ti != idx and len(l) == len(rsurfixd[ti]):
                        deld.add(ti)
                        deld.add(idx)
                        
            
        # print(f"deld : {deld}")

        def dfs(i,l):
            # print(f"dfs {i}, {l}")
            if i != -1 and i in deld:
                return
            
            if i != -1:
                c = cd[i]
                l.append(c)
                # print(f"ans push {l}")
                ans.append(tuple(l))

            for ni in ed[i]:
                dfs(ni,l)

            if i != -1:
                l.pop()

        dfs(-1,[])

        return ans