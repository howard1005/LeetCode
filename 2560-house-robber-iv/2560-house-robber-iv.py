class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        ans = inf
        
        l = [(n,i) for i,n in enumerate(nums)]
        l.sort()

        def valid(mi):
            tl = l[:mi+1]
            tl.sort(key=lambda x:x[1])
            vis = set()
            for _,i in tl:
                if i-1 in vis:
                    continue
                vis.add(i)
                if len(vis) >= k:
                    return True
            return False

        lo,hi = k-1,len(l)-1
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = min(ans,l[mi][0])
                hi = mi-1
            else:
                lo = mi+1

        return ans