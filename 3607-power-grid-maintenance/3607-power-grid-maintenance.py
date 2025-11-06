from heapq import heappush,heappop

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []

        pars = [i for i in range(c)]

        def get_par(i):
            tl = []
            while pars[i] != i:
                tl.append(i)
                i = pars[i]
            for j in tl:
                pars[j] = i
            return i

        def union(i,j):
            pi,pj = get_par(i),get_par(j)
            pars[pj] = pi

        for a,b in connections:
            union(a-1,b-1)

        d = defaultdict(list)

        for i in range(c):
            pi = get_par(i)
            heappush(d[pi],i)

        offs = set()

        for op,i in queries:
            i -= 1
            if op == 1:
                if i not in offs:
                    ans.append(i+1)
                else:
                    pi = get_par(i)
                    while d[pi] and d[pi][0] in offs:
                        heappop(d[pi])
                    ans.append(d[pi][0]+1 if d[pi] else -1)
            elif op == 2:
                offs.add(i)
            

        return ans