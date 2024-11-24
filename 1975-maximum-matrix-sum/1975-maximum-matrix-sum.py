class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        
        m,n = len(matrix),len(matrix[0])
        
        mcnt = 0
        cum = 0
        mn = inf

        for i in range(m):
            for j in range(n):
                v = matrix[i][j]
                if v < 0:
                    mcnt += 1
                cum += abs(v)
                mn = min(mn,abs(v))
                
        if mcnt&1:
            ans = cum - mn*2
        else:
            ans = cum
        
        return ans