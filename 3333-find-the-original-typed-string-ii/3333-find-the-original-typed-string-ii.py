class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        ans = 0

        MOD = 1_000_000_007

        l = []

        cnt = 0
        prev = ''
        for c in word:
            if prev == c:
                cnt += 1
            else:
                l.append((prev,cnt))
                cnt = 1
                prev = c
        l.append((prev,cnt))
        # print(l)

        tot = 1
        for _,cnt in l[1:]:
            tot = (tot*cnt) % MOD

        # print(f"tot {tot}")

        if k < len(l):
            return tot

        dp = [[0 for _ in range(k)] for _ in range(min(k,len(l)))]

        f1 = min(l[1][1],k-1)
        for j in range(1,k):
            dp[1][j] = (1 if j <= f1 else 0) + dp[1][j-1]
        for i in range(2,min(k,len(l))):
            for j in range(1,k):
                f = l[i][1]
                dp[i][j] = dp[i-1][j-1] - (dp[i-1][j-f-1] if j-f-1 >=0 else 0) + dp[i][j-1]
                dp[i][j] = (dp[i][j] + MOD) % MOD

        # for r in dp:
        #     print(r)

        
        ans = (tot - dp[-1][-1] + MOD) % MOD
        
        

        return ans