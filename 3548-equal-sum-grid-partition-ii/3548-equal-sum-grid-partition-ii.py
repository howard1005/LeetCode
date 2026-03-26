class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n = len(grid),len(grid[0])

        if m == 1:
            l = grid[0]
            acum = l[0]
            bcum = sum(l) - l[0]
            for j in range(1,n-1):
                if acum == bcum-l[j]:
                    return True
                acum += l[j]
                bcum -= l[j]

        if n == 1:
            l = [grid[i][0] for i in range(m)]
            acum = l[0]
            bcum = sum(l) - l[0]
            for j in range(1,m-1):
                if acum == bcum-l[j]:
                    return True
                acum += l[j]
                bcum -= l[j]

        def proc1():
            l = []
            for i in range(m):
                cum = 0
                for j in range(n):
                    cum += grid[i][j]
                l.append(cum)
            tot = sum(l)
            if tot%2 == 0:
                target = tot//2
                p = 0
                for i in range(len(l)):
                    p += l[i]
                    if p == target:
                        return True

            l = []
            for j in range(n):
                cum = 0
                for i in range(m):
                    cum += grid[i][j]
                l.append(cum)
            tot = sum(l)
            if tot%2 == 0:
                target = tot//2
                p = 0
                for i in range(len(l)):
                    p += l[i]
                    if p == target:
                        return True
            
            return False

        if proc1():
            return True

        for i,j in [(0,0),(0,-1),(-1,0),(-1,-1)]:
            v = grid[i][j]
            grid[i][j] = 0
            if proc1():
                return True
            grid[i][j] = v

        def proc2():
            # print("proc2")
            d = defaultdict(list)
            ad,bd = defaultdict(int),defaultdict(int)
            acum,bcum = 0,0
            for i in range(m):
                for j in range(n):
                    v = grid[i][j]
                    d[i].append((i,j,v))
                    bcum += grid[i][j]
                    bd[v] += 1
            for i in range(m-1):
                for ii,jj,vv in d[i]:
                    acum += vv
                    ad[vv] += 1
                    bcum -= vv
                    bd[vv] -= 1
                diff = abs(acum - bcum)
                # print(j,diff,ad,bd)
                if acum < bcum and i < m-2:
                    if diff in bd and bd[diff]:
                        return True
                elif acum > bcum and i > 0:
                    if diff in ad and ad[diff]:
                        return True

            d = defaultdict(list)
            ad,bd = defaultdict(int),defaultdict(int)
            acum,bcum = 0,0
            for j in range(n):
                for i in range(m):
                    v = grid[i][j]
                    d[j].append((i,j,v))
                    bcum += grid[i][j]
                    bd[v] += 1
            for j in range(n-1):
                for ii,jj,vv in d[j]:
                    acum += vv
                    ad[vv] += 1
                    bcum -= vv
                    bd[vv] -= 1
                diff = abs(acum - bcum)
                # print(j,diff,ad,bd)
                if acum < bcum and j < n-2:
                    if diff in bd and bd[diff]:
                        return True
                elif acum > bcum and j > 0:
                    if diff in ad and ad[diff]:
                        return True

        if m>1 and n>1 and proc2():
            return True



        return False