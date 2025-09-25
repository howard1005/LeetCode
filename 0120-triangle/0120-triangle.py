class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2,-1,-1):
            ur = triangle[i]
            br = triangle[i+1]
            for j in range(len(ur)):
                ur[j] += min(br[j],br[j+1])
        return triangle[0][0]