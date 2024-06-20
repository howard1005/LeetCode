class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        ans = 0

        position.sort()

        def valid(mi):
            mm = m-1
            pp = position[0]
            for p in position[1:]:
                if p-pp >= mi:
                    mm -= 1
                    pp = p
            return mm <= 0
                

        lo,hi = 1,position[-1]-position[0]
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = max(ans,mi)
                lo = mi+1
            else:
                hi = mi-1

        return ans