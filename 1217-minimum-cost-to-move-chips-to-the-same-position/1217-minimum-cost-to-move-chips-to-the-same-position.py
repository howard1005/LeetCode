class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        o,e = 0,0
        for p in position:
            if p&1:
                o+=1
            else:
                e+=1
        return min(o,e)