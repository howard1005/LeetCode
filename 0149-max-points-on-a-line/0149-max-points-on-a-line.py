from decimal import Decimal
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        ans = 0
        
        for i in range(len(points)):
            d = defaultdict(int)
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                if x2 == x1:
                    g = inf
                else:
                    g = Decimal(str(y2-y1))/Decimal(str(x2-x1))
                d[g] += 1
                ans = max(ans,d[g]+1)
                
        return ans