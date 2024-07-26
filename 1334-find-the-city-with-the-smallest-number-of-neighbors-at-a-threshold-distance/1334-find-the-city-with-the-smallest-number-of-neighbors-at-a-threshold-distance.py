class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        ans = -1
        
        d = defaultdict(lambda:inf)

        for a,b,c in edges:
            d[(a,a)] = 0
            d[(a,b)] = c
            d[(b,a)] = c

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    d[(j,k)] = min(d[(j,k)],d[(j,i)]+d[(i,k)])
                    
        l = []
        for j in range(n):
            cnt = 0
            for k in range(n):
                if j == k:
                    continue
                if d[(j,k)] <= distanceThreshold:
                    cnt += 1
            l.append((cnt,j))

        l.sort(key=lambda x: (x[0],-x[1]))
        ans = l[0][1]

        return ans