class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        pars = [_ for _ in range(n)]

        def find_par(i):
            tl = []
            while pars[i] != i:
                tl.append(i)
                i = pars[i]
            for j in tl:
                pars[j] = i
            return i

        def union(i,j):
            pi,pj = find_par(i),find_par(j)
            pars[j] = i
        
        l = [(i,v) for i,v in enumerate(nums)]
        l.sort(key=lambda x:x[1])

        for i in range(len(l)-1):
            a,av = l[i]
            b,bv = l[i+1]
            if abs(av-bv)<=maxDiff:
                union(a,b)

        ans = []

        for a,b in queries:
            ans.append(find_par(a)==find_par(b))

        return ans
            
            
