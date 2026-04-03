from bisect import bisect_left,bisect_right

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        ans = 0

        dp = [[0]*2 for _ in range(len(robots))]

        l = [(r,d) for r,d in zip(robots,distance)]
        l.sort()

        walls.sort()

        # print(l)
        # print(walls)

        def count_walls(a,b):
            i = bisect_left(walls,a)
            j = bisect_right(walls,b)
            return j-i
            

        for i in range(len(robots)-1,-1,-1):
            x,dx = l[i]

            lx = max(0,x-dx,l[i-1][0]+1 if i>0 else 0)
            lcnt = count_walls(lx,x)

            rx = min(x+dx,l[i+1][0]-1 if i+1<len(dp) else inf)
            rcnt = count_walls(x,rx)
            
            ldp = dp[i+1][0] if i+1<len(dp) else 0
            rdp = dp[i+1][1] if i+1<len(dp) else 0

            dp[i][0] = max(lcnt+ldp,rcnt+rdp)

            limit = l[i-1][0]+1 if i>0 else 0
            if i>0:
                px,pdx = l[i-1]
                rpx = px+pdx
                limit = min(rpx,x)+1
            # print(f"i limit",i,limit)

            
            lx = max(0,x-dx,limit) if limit<x else limit
            lcnt = count_walls(lx,x) if lx <= x else 0
            # print("pr",lx,x,lcnt)

            rx = min(x+dx,l[i+1][0]-1 if i+1<len(dp) else inf)
            rcnt = count_walls(x,rx)

            dp[i][1] = max(lcnt+ldp,rcnt+rdp)
            

        # print("dp",dp)
        ans = dp[0][0]
            



        return ans