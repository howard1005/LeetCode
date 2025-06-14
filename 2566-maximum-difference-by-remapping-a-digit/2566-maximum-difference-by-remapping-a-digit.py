class Solution:
    def minMaxDifference(self, num: int) -> int:
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
        for i in range(10):
            mn = min(mn,proc(i,0))
            mx = max(mx,proc(i,9))

        ans = mx-mn

        return ans