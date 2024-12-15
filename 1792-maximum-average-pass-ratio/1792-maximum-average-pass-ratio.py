from heapq import heappush,heappop

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ans = 0

        def up_delta(p,t):
            return (p+1)/(t+1)-p/t
        
        hq = []

        for p,t in classes:
            u = up_delta(p,t)
            heappush(hq,(-u,p,t))

        e = extraStudents
        while e:
            u,p,t = heappop(hq)
            np,nt = p+1,t+1
            nu = up_delta(np,nt)
            heappush(hq,(-nu,np,nt))
            e -= 1

        for _,p,t in hq:
            ans += p/t
        ans /= len(classes)

        return ans