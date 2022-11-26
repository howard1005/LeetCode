from decimal import Decimal
from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        
        d = defaultdict(int)
        for w,h in rectangles:
            d[Decimal(w/h)] += 1
        for n in d.values():
            ans += n*(n-1)//2
            
        # print(d)
            
        return ans