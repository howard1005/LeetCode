# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        d = {}
        def getH(i):
            if i not in d:
                d[i] = mountain_arr.get(i)
            return d[i]
        
        def bis(lo,hi,valid):
            while lo <= hi:
                mi = (lo+hi)//2
                t = valid(mi)
                if t > 0:
                    lo = mi + 1
                elif t < 0:
                    hi = mi - 1
                else:
                    return mi
            return -1
        
        def validTop(mi):
            a,b,c = mountain_arr.get(mi-1),mountain_arr.get(mi),mountain_arr.get(mi+1)
            if a < b and b < c:
                return 1
            elif a > b and a > c:
                return -1
            else:
                return 0
        
        flag = 0
        def valid(mi):
            nonlocal flag
            v = mountain_arr.get(mi)
            if v == target:
                return 0
            elif v < target:
                return 1*flag
            elif v > target:
                return -1*flag
        
        top = bis(1,mountain_arr.length()-2,validTop)
        flag = 1
        left = bis(0,top,valid)
        if left != -1:
            return left
        flag = -1
        right = bis(top,mountain_arr.length()-1,valid)
        if right != -1:
            return right
        
        return -1
        
            