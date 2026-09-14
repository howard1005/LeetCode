class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a = max(rec1[0],rec2[0])
        b = min(rec1[2],rec2[2])
        c = max(rec1[1],rec2[1])
        d = min(rec1[3],rec2[3])
        if a < b and c < d:
            return True
        return False