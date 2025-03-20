class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        ansl = []
        
        pars = [i for i in range(n)]
        opars = [(1<<20)-1 for _ in range(n)]

        def find_par(i):
            tl = []
            while pars[i] != i:
                tl.append(i)
                i = pars[i]
            for j in tl:
                pars[j] = i
            return i

        def union(i,j,c):
            pi,pj = find_par(i),find_par(j)
            pars[pj] = pi
            opars[pi] &= opars[pj]&c

        for a,b,c in edges:
            union(a,b,c)

        for a,b in query:
            pa,pb = find_par(a),find_par(b)
            if pa == pb:
                ansl.append(opars[pa])
            else:
                ansl.append(-1)

        return ansl
