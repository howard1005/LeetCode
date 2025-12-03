from math import gcd

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        ans = 0

        def norm(x1,y1,x2,y2):
            a,b = x2-x1,y2-y1
            if a == 0:
                return (0,1)
            elif b == 0:
                return (1,0)
            g = gcd(abs(a),abs(b))
            a //= g
            b //= g
            if a<0:
                a *= -1
                b *= -1
            return (a,b)

        def idx(x1,y1,x2,y2):
            v = norm(x1,y1,x2,y2)
            # print(f"norm: {v}")
            return v[0]*y1-v[1]*x1

        def length(x1,y1,x2,y2):
            a,b = x2-x1,y2-y1
            return a*a+b*b

        def up(d1,d2):
            for k,v in d2.items():
                d1[k] += v

        d = defaultdict(list)
        
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                v = norm(x1,y1,x2,y2)
                d[v].append((i,j))

        # print(d)

        sd = set()

        zans = 0
        for v,l in d.items():
            dd = defaultdict(int)
            ldd = defaultdict(lambda:defaultdict(int))
            size = len(l)
            # print(f"v: {v}")
            for a in range(size):
                i,j = l[a]
                x1,y1 = points[i]
                x2,y2 = points[j]
                h = idx(x1,y1,x2,y2)
                # print(x1,y1,x2,y2,h)
                dd[h] += 1
                le = length(x1,y1,x2,y2)
                ldd[h][le] += 1
            # print(f"dd : {dd}")
            cum = 0
            cd = defaultdict(int)
            for h,cnt in dd.items():
                ans += cum*cnt

                ld = ldd[h]
                for le,lcnt in ld.items():
                    zans += cd[le]*lcnt

                up(cd,ld)
                cum += cnt

        return ans-zans//2