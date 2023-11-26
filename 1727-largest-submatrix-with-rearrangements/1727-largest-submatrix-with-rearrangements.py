class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        
        r,c = len(matrix),len(matrix[0])
        
        for j in range(c):
            for i in range(1,r):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
                    
        for l in matrix:
            l.sort(reverse=True)
            t = inf
            for i,n in enumerate(l):
                t = min(t,n)
                ans = max(ans,(i+1)*t)
        
        return ans
