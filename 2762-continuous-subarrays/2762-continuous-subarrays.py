from heapq import heappush,heappop

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        
        mnq,mxq = [],[]
        vis = set()

        def get_min():
            while mnq and mnq[0][1] in vis:
                heappop(mnq)
            return mnq[0][0]

        def get_max():
            while mxq and mxq[0][1] in vis:
                heappop(mxq)
            return -mxq[0][0]

        dq = deque()
        
        for i,n in enumerate(nums):
            dq.append((n,i))
            heappush(mnq,(n,i))
            heappush(mxq,(-n,i))
            while mnq and mxq and abs(get_min()-get_max()) > 2:
                _,pi = dq.popleft()
                vis.add(pi)
            ans += len(dq)
            
        return ans
            
                

                
                
