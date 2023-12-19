class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img),len(img[0])
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                cum = 0
                cnt = 0
                for a in range(-1,2):
                    for b in range(-1,2):
                        ii,jj = i+a,j+b
                        if ii < 0 or ii >= m or jj < 0 or jj >= n:
                            continue
                        cum += img[ii][jj]
                        cnt += 1
                ans[i][j] = cum//cnt
        
        return ans
                