from heapq import heappush,heappop

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        hq = []
        for n,cnt in d.items():
            heappush(hq,(-cnt,n))
            
        print(hq)
        
        while len(hq)>1:
            cnt1,n1 = heappop(hq)
            cnt2,n2 = heappop(hq)
            if cnt1+1:
                heappush(hq,(cnt1+1,n1))
            if cnt2+1:
                heappush(hq,(cnt2+1,n2))
        
        return -hq[0][0] if hq else 0
                   