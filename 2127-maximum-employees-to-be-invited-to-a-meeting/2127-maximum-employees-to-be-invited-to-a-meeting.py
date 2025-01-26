class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        ans = 0

        def longCycle():
            ret = 0
            vis = set()
            for i in range(len(favorite)):
                if i in vis:
                    continue
                vis.add(i)
                d = {i:0}
                while 1:
                    if favorite[i] in vis:
                        if favorite[i] in d:
                            ret = max(ret,d[i]-d[favorite[i]]+1)
                        break
                    vis.add(favorite[i])
                    d[favorite[i]] = d[i] + 1
                    i = favorite[i]
            return ret

        lc = longCycle()

        print(lc)

        def longNoCycles():
            ret = 0

            endList = set()
            ed = defaultdict(set)
            for i in range(len(favorite)):
                j = favorite[i]
                if favorite[j] == i:
                    t = tuple(sorted([i,j]))
                    endList.add(t)
                ed[j].add(i)
            
            vis = set()

            def bfs(i):
                ret = 0
                dq = deque([(i,0)])
                while dq:
                    i,c = dq.popleft()
                    ret = max(ret,c)
                    for j in ed[i]:
                        if j in vis:
                            continue
                        vis.add(j)
                        dq.append((j,c+1))
                return ret

            for i,j in endList:
                vis.add(i)
                vis.add(j)
                ret += bfs(i)+bfs(j)+2

            return ret

        lnc = longNoCycles()

        ans = max(lc,lnc)

        return ans