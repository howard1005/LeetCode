class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        
        def valid(sy,sx,ey,ex,x,y):
            return not (ey<=y and y<=sy and sx<=x and x<=ex)

        
        for i in range(len(points)):
            sx,sy = points[i]
            for j in range(len(points)):
                if i == j:
                    continue
                ex,ey = points[j]
                if not (sx<=ex and sy>=ey):
                    continue
                flag = True
                for k in range(len(points)):
                    if k == i or k == j:
                        continue
                    x,y = points[k]
                    if not valid(sy,sx,ey,ex,x,y):
                        flag = False
                        break
                if flag:
                    ans += 1

        return ans