class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return False if t == 1 else True
        dx,dy = abs(sx-fx),abs(sy-fy)
        return max(dx,dy) <= t