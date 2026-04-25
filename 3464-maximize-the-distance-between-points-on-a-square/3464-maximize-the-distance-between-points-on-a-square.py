class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        ans = 0 
        
        d = defaultdict(list)
        for p in points:
            if p[1] == side:
                d[0].append(p)
            elif p[0] == side:
                d[1].append(p)
            elif p[1] == 0:
                d[2].append(p)
            elif p[0] == 0:
                d[3].append(p)
        d[0].sort()
        d[1].sort(reverse=True)
        d[2].sort(reverse=True)
        d[3].sort()
        l = d[0]+d[1]+d[2]+d[3]
        # print("l: ",l)

        def valid(n):
            pl = [-1 for _ in range(len(l))]
            i = 0
            for j in range(1,len(pl)):
                x,y = l[j]
                if i >= len(l):
                    break
                px,py = l[i]
                dis = abs(x-px)+abs(y-py)
                while dis >= n:
                    pl[i] = j
                    i += 1
                    if i == j:
                        break
                    if i >= len(l):
                        break
                    px,py = l[i]
                    dis = abs(x-px)+abs(y-py)
            # print("n,pl",n,pl)

            for si in range(len(l)):
                cnt = 1
                hl = [l[si]]
                # print("hit0",l[si])
                i = si
                while cnt < k:
                    i = pl[i]
                    if i == -1:
                        break
                    x,y = l[i]
                    px,py = hl[-1]
                    cnt += 1
                    hl.append(l[i])
                if cnt == k:
                    hx,hy = hl[0]
                    hdis = abs(x-hx)+abs(y-hy)
                    # print("hhit",cnt,l[i],hdis)
                    if hdis >= n:
                        return True
            return False

        lo,hi = 1,side
        while lo<=hi:
            mi = (lo+hi)//2
            f = valid(mi)
            # print(mi,f)
            if f:
                ans = max(ans,mi)
                lo = mi+1
            else:
                hi = mi-1
        
        return ans