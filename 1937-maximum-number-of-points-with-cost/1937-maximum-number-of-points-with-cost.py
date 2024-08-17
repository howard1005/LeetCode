class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 특정 pivot 을 중심으로 일정 크기의 증감은 좌/우로 피벗을 설정했을때의 순서와 같다 라는 아이디어

        r,c = len(points),len(points[0])

        dp = [[0 for _ in range(c)] for _ in range(r)]

        def make_pivotl(l):
            al = []
            mxi = -1
            mx = -inf
            for i in range(len(l)):
                v = l[i]-(len(l)-i-1)
                if v > mx:
                    mxi = i
                    mx = v
                al.append((mxi,mx,l[mxi]))

            rl = list(reversed(l))
            bl = []
            mxi = -1
            mx = -inf
            for i in range(len(rl)):
                v = rl[i]-(len(rl)-i-1)
                if v > mx:
                    mxi = len(rl)-i-1
                    mx = v
                bl.append((mxi,mx,l[mxi]))
            bl.reverse()

            return al,bl
        
        def max_by_pivot(al,bl,p):
            ai,_,av = al[p]
            bi,_,bv = bl[p]
            amx = av-abs(ai-p)
            bmx = bv-abs(bi-p)
            if amx > bmx:
                return (ai,amx)
            else:
                return (bi,bmx)

        al,bl = make_pivotl(points[-1])
        # print(al,bl)
        for j in range(c):
            mxi,mx = max_by_pivot(al,bl,j)
            dp[-1][j] = mx
                

        for i in range(r-2,-1,-1):
            al,bl = make_pivotl([v+dpv for v,dpv in zip(points[i],dp[i+1])])
            for j in range(c):
                mxi,mx = max_by_pivot(al,bl,j)
                dp[i][j] = mx

        # for r in dp:
        #     print(r)

        return max(dp[0])

        
        