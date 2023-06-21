from bisect import bisect_right

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        ans = 0
        
        l = sorted([(n,c) for n,c in zip(nums,cost)])
        cums = [l[i][1] for i in range(len(l))]
        for i in range(1,len(cums)):
            cums[i] += cums[i-1]
        
        i = bisect_right(cums,cums[-1]/2)
        if i == len(cums):
            i-=1
        
        t = l[i][0]

        for n,c in l:
            ans += abs(n-t)*c
            
        return ans