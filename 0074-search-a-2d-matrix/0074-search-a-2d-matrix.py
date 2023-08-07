class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c= len(matrix),len(matrix[0])
        n = r*c
        def pos(i):
            return (i//c,i%c)
        lo,hi = 0,n-1
        while lo<=hi:
            mi = (lo+hi)//2
            y,x = pos(mi)
            if matrix[y][x] < target:
                lo = mi+1
            elif matrix[y][x] > target:
                hi = mi-1
            else:
                return True
        return False