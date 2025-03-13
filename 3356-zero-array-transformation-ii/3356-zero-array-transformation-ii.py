class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        ans = inf

        def valid(k):
            l = [0 for _ in range(len(nums))]
            for i in range(k):
                a,b,c = queries[i]
                l[a] += c
                if b+1 < len(l):
                    l[b+1] -= c
            for i in range(len(l)):
                if i-1 >= 0:
                    l[i] += l[i-1]
                if l[i] < nums[i]:
                    return False
            return True

        lo,hi = 0,len(queries)
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = min(ans,mi)
                hi = mi-1
            else:
                lo = mi+1

        return ans if ans != inf else -1

