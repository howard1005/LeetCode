class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z = 0
        for c in s:
            if c == '0':
                z += 1
        if z == 0:
            return 0

        le = len(s)

        ans = 0

        

        def bfs():
            vis = defaultdict(lambda:x)
            osl = SortedList([i for i in range(1,le+1,2)])
            esl = SortedList([i for i in range(0,le+1,2)])

            if z&1:
                osl.remove(z)
            else:
                esl.remove(z)
            vis[z] = 0
            dq = deque([(z,0)])
            while dq:
                ze,cost = dq.popleft()
                # print(ze,cost,sl,dq)
                o = le-ze
                a,b = max(0,k-o),min(k,ze)
                mnz = ze+k-2*b
                mxz = ze+k-2*a
                sl =  osl if mnz&1 else esl
                i = sl.bisect_left(mnz)
                j = sl.bisect_right(mxz)
                # print("mnz,mxz,i,j",mnz,mxz,i,j)
                if i>=len(sl):
                    continue
                dl = []
                for ii in range(i,j):
                    # print(ii,sl)
                    nz = sl[ii]
                    nc = cost+1
                    if nz == 0:
                        return nc
                    if nz in vis:
                        continue
                    dl.append(nz)
                    vis[nz] = nc
                    dq.append((nz,nc))
                for dz in dl:
                    sl.remove(dz)

            return -1

        ans = bfs()
                
            
        return ans