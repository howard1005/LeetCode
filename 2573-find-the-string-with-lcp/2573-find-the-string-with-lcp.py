class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        
        for i in range(n):
            if lcp[i][i] != n-i:
                return ''

        for i in range(n):
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ''
                if lcp[i][j] > min(n-i,n-j):
                    return ''

        for j in range(1,n):
            ii = 0
            cnt = 0
            for jj in range(j,n):
                if cnt:
                    if cnt-1 != lcp[ii][jj]:
                        return ''
                    cnt -= 1
                else:
                    cnt = lcp[ii][jj]
                ii += 1
            if cnt > 1:
                return ''

        ans = ''

        pars = [i for i in range(n)]

        def find(i):
            tl = []
            while i != pars[i]:
                tl.append(i)
                i = pars[i]
            for j in tl:
                pars[j] = i
            return i

        def union(i,j):
            pi,pj = find(i),find(j)
            pars[pj] = pi

        def isUnion(i,j):
            return find(i) == find(j)

        dis = []
        for i in range(n):
            for j in range(i+1,n):
                if lcp[i][j]:
                    union(i,j)
                else:
                    dis.append((i,j))
        for i,j in dis:
            if isUnion(i,j):
                return ''
        
        d = {}
        for i in range(n):
            pi = find(i)
            if pi not in d:
                c = chr(ord('a') + len(d))
                if c > 'z':
                    return ''
                d[pi] = c
            ans += d[pi]
                    
        return ans
