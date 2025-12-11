class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        ans = 0

        xd,yd = defaultdict(lambda:[inf,-inf]),defaultdict(lambda:[inf,-inf])

        for x,y in buildings:
            xd[x][0] = min(xd[x][0],y)
            xd[x][1] = max(xd[x][1],y)
            yd[y][0] = min(yd[y][0],x)
            yd[y][1] = max(yd[y][1],x)

        for x,y in buildings:
            if xd[x][0] < y and y < xd[x][1] and yd[y][0] < x and x < yd[y][1]:
                ans += 1
            
        return ans