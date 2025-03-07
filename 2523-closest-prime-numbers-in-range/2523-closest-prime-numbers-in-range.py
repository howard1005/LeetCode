class Solution:
    ps = []
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if not self.ps:
            n = 1000000
            sd = set(range(3,n+1,2))
            sd.add(2)
            i = 3
            while i*i <= n:
                if i in sd:
                    sd -= set(range(i*2,n+1,i))
                i += 2
            self.ps = list(sd)
            self.ps.sort()

        ps = self.ps

        ans = [inf,inf,inf]

        for i in range(len(ps)-1):
            a,b = ps[i],ps[i+1]
            if left<=a and b<=right:
                ans = min(ans,[b-a,a,b])
        
        if ans[0] == inf:
            return [-1,-1]

        return ans[1:]

        

        