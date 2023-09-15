import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ans = 0
        h = []
        vis = [0 for _ in range(len(points))]
        edges = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                d = abs(x1-x2)+abs(y1-y2)
                edges[i].append((d,j))
                edges[j].append((d,i))
        heapq.heappush(h,(0,0))
        while h:
            d,n = heapq.heappop(h)
            if vis[n]:
                continue
            vis[n] = 1
            ans += d
            for edge in edges[n]:
                nd,nn = edge
                if not vis[nn]:
                    heapq.heappush(h,(nd,nn))
        return ans