from bisect import bisect_right

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        ans = 0
        
        l = [(i-r,i+r) for i,r in enumerate(ranges)]
        l.sort()
        
        mxl = [b for a,b in l]
        for i in range(1,len(mxl)):
            mxl[i] = max(mxl[i],mxl[i-1])
            
        i = 0
        while i < n:
            j = bisect_right(l,i,key=lambda x: x[0])
            if j > 0:
                ans += 1
                ni = mxl[j-1]
                if ni <= i:
                    return -1
                i = ni
            else:
                return -1
        
        return ans