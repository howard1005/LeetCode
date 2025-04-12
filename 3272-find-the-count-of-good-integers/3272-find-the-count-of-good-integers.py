from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        end = n//2 + (1 if n&1 else 0)
        print(end)

        @cache
        def dfs(i,m,t):
            if i == end:
                if m == 0:
                    print(i,m,t)
                    ret = factorial(n) - t[0]*factorial(n-1)
                    for cnt in t:
                        ret //= factorial(cnt)
                    return ret
                return 0
            ret = 0
            
            for j in range((0 if i else 1),10):
                q = j*10**(n-i-1)
                tl = list(t)
                tl[j] += 1
                if n&1 and i==end-1:
                    pass
                else:
                    q += j*10**i
                    tl[j] += 1
                nt = tuple(tl)
                ret += dfs(i+1,(m+q)%k,nt)
            print(i,m,ret)
            return ret
        
        ans = dfs(0,0,tuple(0 for _ in range(10)))

        return ans
                