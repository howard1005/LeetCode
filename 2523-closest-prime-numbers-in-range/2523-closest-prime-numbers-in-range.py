class Solution:
    ps = []
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ps = self.ps
        if not ps:
            def isP(n):
                i = 2
                while i*i <= n:
                    if n%i == 0:
                        return False
                    i += 1
                return True
            ps.append(2)
            for i in range(3,1000001,2):
                if isP(i):
                    ps.append(i)

        ans = [inf,inf,inf]

        for i in range(len(ps)-1):
            a,b = ps[i],ps[i+1]
            if left<=a and b<=right:
                ans = min(ans,[b-a,a,b])
        
        if ans[0] == inf:
            return [-1,-1]

        return ans[1:]

        

        