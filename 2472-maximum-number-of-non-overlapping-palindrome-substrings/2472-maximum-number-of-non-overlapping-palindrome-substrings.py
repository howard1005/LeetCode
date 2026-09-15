class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        ans = 0

        dp = [0 for _ in range(len(s))]
        dp[-1] = 1 if k == 1 else 0

        od = {}
        ed = {}

        for i in range(len(s)):
            a,b = i,i
            while a>=0 and b<len(s) and s[a]==s[b]:
                a-=1
                b+=1
            a += 1
            b -= 1
            if b-a+1 < k:
                continue
            od[i] = (a,b)
        
        for i in range(len(s)-1):
            a,b = i,i+1
            if s[a]!=s[b]:
                continue
            while a>=0 and b<len(s) and s[a]==s[b]:
                a-=1
                b+=1
            a += 1
            b -= 1
            if b-a+1 < k:
                continue
            ed[i] = (a,b)

        # print(od)
        # print(ed)

        for i in range(len(s)-2,-1,-1):
            dp[i] = dp[i+1]
            for j in range(i+k-1,len(s)):
                p = (i+j)//2
                size = j-i+1
                if size%2==1 and p in od and od[p][0] <= i and i <= od[p][1]:
                    dp[i] = max(dp[i],1+(dp[j+1] if j+1<len(dp) else 0))
                if size%2==0 and p in ed and ed[p][0] <= i and i <= ed[p][1]:
                    dp[i] = max(dp[i],1+(dp[j+1] if j+1<len(dp) else 0))

        # print(dp)
                
        ans = dp[0]

        return ans