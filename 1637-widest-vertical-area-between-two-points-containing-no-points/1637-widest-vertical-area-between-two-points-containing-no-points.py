class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = 0
        
        points.sort()
        for i in range(len(points)-1):
            ans = max(ans,points[i+1][0]-points[i][0])
        
        return ans
            
            