class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        tail = float('inf')
        for point in points:
            if point[0] > tail:
                ans += 1
                tail = point[1]
            else:
                tail = min(tail, point[1])
        return ans + 1