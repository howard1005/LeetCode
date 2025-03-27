from heapq import heappop,heappush

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        ld,rd = defaultdict(int),defaultdict(int)
        lhq,rhq = [],[]

        for n in nums:
            rd[n] += 1
        for n,cnt in rd.items():
            heappush(rhq,(-cnt,n))

        def top(hq,d):
            while hq and d[hq[0][1]] != -hq[0][0]:
                heappop(hq)
            return hq[0]

        for i,n in enumerate(nums[:-1]):
            ld[n] += 1
            heappush(lhq,(-ld[n],n))
            rd[n] -= 1
            heappush(rhq,(-rd[n],n))
            lcnt,ln = top(lhq,ld)
            lcnt = -lcnt
            rcnt,rn = top(rhq,rd)
            rcnt = -rcnt
            
            if ln != rn:
                continue
            lsize = i+1
            rsize = len(nums)-lsize
            if lcnt*2>lsize and rcnt*2>rsize:
                return i
        
        return -1


            