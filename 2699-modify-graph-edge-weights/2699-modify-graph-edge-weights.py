from heapq import heappush,heappop

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        ansl = []

        MAXC = 1000000000

        ed = defaultdict(set)
        cd = defaultdict(int)

        for a,b,c in edges:
            ed[a].add(b)
            ed[b].add(a)
            if c > 0:
                cd[(a,b)] = c
                cd[(b,a)] = c
            else:
                cd[(a,b)] = MAXC
                cd[(b,a)] = MAXC

        def dijk():
            vis = defaultdict(lambda:inf)
            vis[source] = 0
            hq = [(0,source)]

            while hq:
                c,i = heappop(hq)
                # print("dijk",c,i)
                if i == destination:
                    # print("return",c)
                    return c
                if c > vis[i]:
                    continue
                for ni in ed[i]:
                    nc = cd[(i,ni)]
                    if vis[ni] > c + nc:
                        vis[ni] = c + nc
                        heappush(hq,(c+nc,ni))

        def update(a,b,c):
            cd[(a,b)] = c
            cd[(b,a)] = c

        def proc(a,b,c):
            lo,hi = 1,c
            # print(a,b,c,lo,hi)
            mi = -1
            while lo<=hi:
                mi = (lo+hi)//2
                # print(mi)

                update(a,b,mi)

                mc = dijk()
                # print("mc : ", mc)
                if mc < target:
                    lo = mi + 1
                elif mc > target:
                    hi = mi - 1
                else:
                    return mi

            return mi

        l = []
        for a,b,c in edges:
            if c == -1:
                l.append([a,b,MAXC])
            else:
                ansl.append((a,b,c))

        def proc2():
            reti = -1
            lo,hi = 0,len(l)
            while lo<=hi:
                mi = (lo+hi)//2
                for a,b,c in l[:mi]:
                    update(a,b,1)
                mc = dijk()
                # print("proc2 mc",mc)
                if mc < target:
                    reti = mi-1
                    hi = mi - 1
                elif mc > target:
                    lo = mi + 1
                else:
                    return mi-1
                for a,b,c in l[:mi]:
                    update(a,b,MAXC)
            return reti

        i = proc2()
        # print("i",i)
        for j in range(i):
            a,b,_ = l[j]
            update(a,b,1)
            l[j][2] = 1
        if i >= 0:
            a,b,c = l[i]
            fixc = proc(a,b,c)
            # print("fixc",fixc)
            l[i][2] = fixc

        ansl.extend(l)

        if dijk() != target:
            return []

        return ansl