class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l = []
        for r in grid:
            for n in r:
                l.append(n)
        l.sort()

        ll = [0 for _ in range(len(l))]
        for i,n in enumerate(l):
            pn = l[i-1]
            diff = n-pn
            if diff%x:
                return -1
            cum = diff*i
            ll[i] = ll[i-1] + cum//x

        rl = [0 for _ in range(len(l))]
        for i in range(len(l)-2,-1,-1):
            n = l[i]
            pn = l[i+1]
            diff = pn-n
            if diff%x:
                return -1
            cum = diff*(len(l)-i-1)
            rl[i] = rl[i+1] + cum//x

        ans = inf
        for i in range(len(l)):
            ans = min(ans,ll[i]+rl[i])
            
        return ans