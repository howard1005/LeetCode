class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0

        def sq(m):
            x = 1
            while x*x < m:
                x += 1
            if x*x == m:
                return x
            return None

        for a in range(1,n+1):
            for b in range(1,n+1):
                c = sq(a*a+b*b)
                if c and c <= n:
                    ans += 1
                
        return ans