class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        ans = 0

        restrictions.sort()

        # print(restrictions)

        for i in range(len(restrictions)-2,-1,-1):
            r1,r2 = restrictions[i],restrictions[i+1]
            j1,j2 = r1[0],r2[0]
            h1,h2 = r1[1],r2[1]
            if h1 <= h2:
                continue
            le = j2-j1
            r1[1] = min(h1,h2+le)
        
        # print(restrictions)

        i = 0
        h = 0
        for ti,th in restrictions:
            ti -= 1
            le = ti-i
            # print('ti,th,le',ti,th,le)
            if h <= th:
                r = le-(th-h)-1
                # print('inc r',r)
                if r > 0:
                    ans = max(ans,th+r//2+(1 if r&1 else 0))
                    h = th
                else:
                    h = min(th,h+le)
                    ans = max(ans,h)
            else:
                r = le-(h-th)-1
                # print('dec r',r)
                if r > 0:
                    ans = max(ans,h+r//2+(1 if r&1 else 0))
                    h = th
                else:
                    h = max(th,h-le)
                    ans = max(ans,h)
            i = ti
            # print(i,h,ans,'\n')

        ans = max(ans,n-1-i+h)
            

        return ans