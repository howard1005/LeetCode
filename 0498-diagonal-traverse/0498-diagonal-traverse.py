class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []

        m,n = len(mat),len(mat[0])
        
        for t in range(0,m+n):
            imx,jmx = min(m-1,t),min(n-1,t)
            if t%2:
                i,j = t-jmx,jmx
                while i<=imx:
                    ans.append(mat[i][j])
                    i += 1
                    j -= 1
            else:
                i,j = imx,t-imx
                while j<=jmx:
                    ans.append(mat[i][j])
                    i -= 1
                    j += 1


        return ans