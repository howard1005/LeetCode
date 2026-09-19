class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        if x1 <= xCenter and xCenter <= x2 and y1 <= yCenter and yCenter <= y2:
            return True

        a,b,c,d = x1-xCenter,y1-yCenter,x2-xCenter,y2-yCenter
        r = radius

        # print(a,b,c,d)

        if a>0 and b<=0 and d>=0:
            if a <= r:
                return True
        if d<0 and a<=0 and c>=0:
            if -d <= r:
                return True
        if c<0 and b<=0 and d>=0:
            if -c <= r:
                return True
        if b>0 and a<=0 and c>=0:
            if b <= r:
                return True

        if a>0 and b>0:
            if a**2+b**2 <= r**2:
                return True
        if a>0 and d<0:
            if a**2+d**2 <= r**2:
                return True
        if c<0 and d<0:
            if c**2+d**2 <= r**2:
                return True
        if c<0 and b>0:
            if c**2+b**2 <= r**2:
                return True

        return False