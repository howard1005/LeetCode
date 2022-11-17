class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        ix1 = max(ax1,bx1)
        iy1 = max(ay1,by1)
        ix2 = min(ax2,bx2)
        iy2 = min(ay2,by2)
        def area(x1,y1,x2,y2):
            if x1>=x2 or y1>=y2: return 0
            return abs(x1-x2)*abs(y1-y2)
        return area(ax1,ay1,ax2,ay2)+area(bx1,by1,bx2,by2)-area(ix1,iy1,ix2,iy2)