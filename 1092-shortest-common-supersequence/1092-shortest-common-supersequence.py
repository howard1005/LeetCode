class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        ans = ''

        dp = [[(-1,-1,-1,'') for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
        for i in range(len(str1)):
            dp[i][-1] = (len(str1)-i,i+1,len(str2),str1[i])
        for j in range(len(str2)):
            dp[-1][j] = (len(str2)-j,len(str1),j+1,str2[j])
        dp[-1][-1] = (0,-1,-1,'')

        for i in range(len(str1)-1,-1,-1):
            for j in range(len(str2)-1,-1,-1):
                a,b = str1[i],str2[j]
                if a == b:
                    t = dp[i+1][j+1]
                    dp[i][j] = (1+t[0],i+1,j+1,a)
                else:
                    ta = dp[i+1][j]
                    tb = dp[i][j+1]
                    if ta[0] < tb[0]:
                        dp[i][j] = (1+ta[0],i+1,j,a)
                    else:
                        dp[i][j] = (1+tb[0],i,j+1,b)

        i,j = 0,0
        while i!=-1:
            _,ni,nj,c = dp[i][j]
            
            ans += c

            i,j = ni,nj
            
        
        return ans