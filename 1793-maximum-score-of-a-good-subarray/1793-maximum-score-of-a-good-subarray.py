from heapq import heappop,heappush

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = 0
        
        hq = []
        for i,n in enumerate(nums):
            heappush(hq,(n,i))
        
        s,e = 0,len(nums)-1
        
        def top():
            while hq and (hq[0][1] < s or e < hq[0][1]):
                heappop(hq)
            if hq:
                return hq[0]
            return None
        
        def valid(i,j):
            nonlocal s,e
            if i<=j and i<=k and k<=j:
                s,e = i,j
                return True
            return False
                
        def div(tl):
            nonlocal s,e
            i = s
            for di in tl:
                j = di-1
                if valid(i,j):
                    return True
                i = di+1
            if valid(i,e):
                return True
            return False
        
        while hq:
            t = top()[0]
            ans = max(ans,t*(e-s+1))
            
            tl = []
            while top() and top()[0] == t:
                tl.append(heappop(hq)[1])
                    
            if div(tl) == False:
                break

        return ans