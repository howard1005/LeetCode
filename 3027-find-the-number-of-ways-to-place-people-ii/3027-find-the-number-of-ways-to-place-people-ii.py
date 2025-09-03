class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0

        points.sort(key=lambda x: (x[0],-x[1]))

        for i in range(len(points)):
            x1,y1 = points[i]
            py2 = -inf
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                if py2 < y2 and y2 <= y1:
                    ans += 1
                    py2 = y2  

        return ans