from heapq import heappush,heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        
        l = [(n1,n2) for n1,n2 in zip(nums1,nums2)]
        l.sort(key=lambda x: -x[1])
        
        hq = []
        cum = 0
        for i in range(len(l)):
            n1,n2 = l[i]
            if len(hq) < k:
                cum += n1
                heappush(hq,n1)
            else:
                if hq[0] < n1:
                    cum -= heappop(hq)
                    cum += n1
                    heappush(hq,n1)
            if len(hq) == k:
                ans = max(ans,cum*n2)
                
        return ans