class Solution:
    def maxDiff(self, num: int) -> int:
        l = []

        while num:
            l.append(num%10)
            num //= 10

        l.reverse()
        
        def proc(a,b):
            ret = 0
            for n in l:
                if n == a:
                    n = b
                ret = ret*10+n
            return ret

        mn,mx = inf,0
        for a in range(10):
            for b in range(10):
                if l[0] == a and b == 0:
                    continue
                t = proc(a,b)
                if t:
                    mn = min(mn,t)
                    mx = max(mx,t)

        ans = mx-mn

        return ans
            