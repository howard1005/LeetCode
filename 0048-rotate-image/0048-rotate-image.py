class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        r,c -> c,n-r
        """
        
        n = len(matrix)
        
        def proc(i,j):
            t = matrix[i][j]
            for _ in range(4):
                i,j = j,n-i-1
                tt = matrix[i][j]
                matrix[i][j] = t
                t = tt
                
        for i in range((n+1)//2):
            for j in range(i,n-i-1):
                proc(i,j)
        