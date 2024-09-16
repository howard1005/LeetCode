class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ans = inf

        l = []
        for t in timePoints:
            ts = t.split(':')
            m = int(ts[0])*60+int(ts[1])
            l.append(m)

        l.sort()
        ans = 1440-(l[-1]-l[0])

        for i in range(1,len(l)):
            ans = min(ans,l[i]-l[i-1])
        
        return ans