class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        r,c = len(rowSum),len(colSum)

        ans = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r):
            rs = rowSum[i]
            for j in range(c):
                t = min(rs,colSum[j])
                ans[i][j] = t
                rs -= t
                colSum[j] -= t
        
        return ans
                
        