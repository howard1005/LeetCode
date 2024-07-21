class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(k)] for _ in range(k)]

        rindd,cindd = defaultdict(int),defaultdict(int)
        red,ced = defaultdict(set),defaultdict(set)

        for a,b in rowConditions:
            if b not in red[a]:
                rindd[b] += 1
                red[a].add(b)
            
        for a,b in colConditions:
            if b not in ced[a]:
                cindd[b] += 1
                ced[a].add(b)

        # print(rindd)
        # print(cindd)

        def proc(indd,ed):
            retl = []
            dq = deque()
            for n in range(1,k+1):
                if indd[n] == 0:
                    dq.append(n)
            while dq:
                n = dq.popleft()
                retl.append(n) 
                for nn in ed[n]:
                    indd[nn] -= 1
                    if indd[nn] == 0:
                        dq.append(nn)
            # print("proc indd : ", indd)
            for n,v in indd.items():
                if v != 0:
                    return -1
            return retl

        rl = proc(rindd,red)
        cl = proc(cindd,ced)

        # print(rl,cl)

        if rl == -1 or cl == -1:
            return []

        d = defaultdict(lambda:[-1,-1])
        for i,n in enumerate(rl):
            d[n][0] = i
        for i,n in enumerate(cl):
            d[n][1] = i

        for n,(i,j) in d.items():
            ans[i][j] = n

        return ans
                