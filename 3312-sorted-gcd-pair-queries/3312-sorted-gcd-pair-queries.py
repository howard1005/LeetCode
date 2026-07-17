from bisect import bisect_left
from math import gcd

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []

        d = defaultdict(int)
        for n in nums:
            d[n] += 1
            
        mx = max(nums)

        gl = [0 for _ in range(mx+1)]
        
        for g in range(mx,0,-1):
            m = 0
            for i in range(g, mx + 1, g):
                m += d[i]
            cnt = m * (m - 1) // 2
            for i in range(g * 2, mx + 1, g):
                cnt -= gl[i]
            gl[g] = cnt
        
        # print(gl)

        gl[0] = -1
        mni = 0
        for i in range(1,len(gl)):
            gl[i] += gl[i-1]
            if mni == 0 and gl[i]>=0:
                mni = i
        
        # print(gl,mni)
            
        for q in queries:
            i = bisect_left(gl,q,mni,len(gl))
            ans.append(i)

        return ans