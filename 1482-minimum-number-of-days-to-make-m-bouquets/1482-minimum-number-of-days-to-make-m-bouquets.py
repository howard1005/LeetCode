class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ans = inf

        def valid(t):
            mm = m
            l = []
            for b in bloomDay:
                l.append(1 if b <= t else 0)
            cnt = 0
            for o in l:
                if o:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == k:
                    mm -= 1
                    cnt = 0
            if mm <= 0:
                return True
                    

        lo,hi = 0,max(bloomDay)
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                hi = mi-1
                ans = min(ans,mi)
            else:
                lo = mi+1


        return ans if ans != inf else -1