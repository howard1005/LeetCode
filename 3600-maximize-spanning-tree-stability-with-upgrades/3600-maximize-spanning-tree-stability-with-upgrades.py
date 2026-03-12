from heapq import heappush,heappop

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        ans = 0
        
        pars = [i for i in range(n)]

        def find(i):
            tl = []
            while pars[i] != i:
                tl.append(i)
                i = pars[i]
            for j in tl:
                pars[j] = i
            return i

        def union(i,j):
            pi,pj = find(i),find(j)
            pars[pj] = pi

        def valid():
            i = find(0)
            for j in pars:
                if find(j) != i:
                    return False
            return True

        mn = inf
        notmusts = []
        conn = 0

        for u,v,s,must in edges:
            if must:
                if find(u) == find(v):
                    return -1
                union(u,v)
                conn += 1
                mn = min(mn,s)
            else:
                notmusts.append((u,v,s,must))

        # print("mn,conn",mn,conn)

        if notmusts and conn < n-1:
            kcands = []
            notmusts.sort(key=lambda x:-x[2])
            for u,v,s,must in notmusts:
                # print("not must ",u,v,s,must)
                if find(u) == find(v):
                    # print("skip")
                    continue
                union(u,v)
                conn += 1
                heappush(kcands, s)
                if conn == n-1:
                    break
            while kcands and k:
                s = heappop(kcands)
                mn = min(mn,2*s)
                k -= 1
            if kcands:
                mn = min(mn,kcands[0])
            

        # print(pars)

        if not valid():
            return -1

        ans = mn

        return ans
        