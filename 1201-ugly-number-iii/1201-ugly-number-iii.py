class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a, b):
            def gcd(x, y):
                while y:
                    x, y = y, x % y
                return x

            return a * b // gcd(a, b)

        
        def valid(m):
            aa,bb,cc = m//a,m//b,m//c
            mx = max(a*aa,b*bb,c*cc)
            ab,bc,ca = m//lcm(a,b),m//lcm(b,c),m//lcm(c,a)
            abc = m//lcm(lcm(a,b),c)
            return (mx,aa+bb+cc-ab-bc-ca+abc)
        
        
        lo,hi = 0,1000000000000000000
        while lo<=hi:
            mi = (lo+hi)//2
            (v,cnt) = valid(mi)
            if cnt < n:
                lo = mi+1
            elif cnt > n:
                hi = mi-1
            else:
                return v
            
        return -1