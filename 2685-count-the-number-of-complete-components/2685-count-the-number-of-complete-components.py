class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
               
        pars = [i for i in range(n)]

        def find_par(i):
            tl = []
            while i != pars[i]:
                tl.append(i)
                i = pars[i]
            for j in tl:
                pars[j] = i
            return i

        def union(i,j):
            pi,pj = find_par(i),find_par(j)
            pars[pj] = pi

        ed = defaultdict(list)
        for a,b in edges:
            ed[a].append(b)
            ed[b].append(a)
            union(a,b)

        gd = defaultdict(list)
        for i in range(n):
            p = find_par(i)
            gd[p].append(i)

        def valid(l):
            for i in l:
                if len(ed[i]) != len(l)-1:
                    return False
            return True 

        for _,l in gd.items():
            if valid(l):
                ans += 1

        return ans