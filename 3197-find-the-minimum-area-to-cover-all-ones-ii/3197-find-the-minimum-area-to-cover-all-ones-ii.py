class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        ans = inf

        m,n = len(grid),len(grid[0])

        hm = [[grid[i][j] for j in range(n)] for i in range(m)]
        vm = [[grid[i][j] for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                hm[i][j] += (hm[i][j-1] if j > 0 else 0)

        for j in range(n):
            for i in range(m):
                vm[i][j] += (vm[i-1][j] if i > 0 else 0)

        # print("hm")
        # for r in hm:
        #     print(r)

        # print("vm")
        # for r in vm:
        #     print(r)

        def ish(i,j1,j2):
            cum = hm[i][j2] - (hm[i][j1-1] if j1 > 0 else 0)
            return cum > 0

        def isv(i1,i2,j,):
            cum = vm[i2][j] - (vm[i1-1][j] if i1 > 0 else 0)
            return cum > 0


        def area(y1,x1,y2,x2):
            yy1 = y1
            for y in range(y1,y2+1):
                yy1 = y
                if ish(yy1,x1,x2):
                    break
            
            yy2 = y2
            for y in range(y2,y1-1,-1):
                yy2 = y
                if ish(yy2,x1,x2):
                    break

            xx1 = x1
            for x in range(x1,x2+1):
                xx1 = x
                if isv(y1,y2,xx1):
                    break

            xx2 = x2
            for x in range(x2,x1-1,-1):
                xx2 = x
                if isv(y1,y2,xx2):
                    break

            ret = (yy2-yy1+1)*(xx2-xx1+1)

            # print(f"area {y1},{x1},{y2},{x2} -> {yy1},{xx1},{yy2},{xx2} : {ret}")

            return ret if ret > 0 else 0

        

        for i1 in range(m-2):
            a1 = area(0,0,i1,n-1)
            for i2 in range(i1+1,m-1):
                a2 = area(i1+1,0,i2,n-1)
                a3 = area(i2+1,0,m-1,n-1)
                
                ans = min(ans,a1+a2+a3)
                

        for j1 in range(n-2):
            a1 = area(0,0,m-1,j1)
            for j2 in range(j1+1,n-1):
                a2 = area(0,j1+1,m-1,j2)
                a3 = area(0,j2+1,m-1,n-1)
                
                ans = min(ans,a1+a2+a3)

        for i in range(m-1):
            for j in range(n-1):
                # print(f"\n {i},{j} \n")
                a1 = area(0,0,i,n-1)
                a2 = area(i+1,j+1,m-1,n-1)
                a3 = area(i+1,0,m-1,j)
                # print(f"t1 : {a1},{a2},{a3}")
                ans = min(ans,a1+a2+a3)

                a1 = area(0,j+1,m-1,n-1)
                a2 = area(i+1,0,m-1,j)
                a3 = area(0,0,i,j)
                # print(f"t2 : {a1},{a2},{a3}")
                ans = min(ans,a1+a2+a3)
        
                a1 = area(i+1,0,m-1,n-1)
                a2 = area(0,0,i,j)
                a3 = area(0,j+1,i,n-1)
                # print(f"t3 : {a1},{a2},{a3}")
                ans = min(ans,a1+a2+a3)

                a1 = area(0,0,m-1,j)
                a2 = area(0,j+1,i,n-1)
                a3 = area(i+1,j+1,m-1,n-1)
                # print(f"t4 : {a1},{a2},{a3}")
                ans = min(ans,a1+a2+a3)

        return ans