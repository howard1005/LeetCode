from heapq import heappush,heappop

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        lc = len(cookies)
        dp = [[inf for _ in range(1<<lc)] for _ in range(k)]
        cd = {}
        
        for m in range(1<<lc):
            cnt = 0
            mx = 0
            for j in range(lc):
                if (m>>j)&1:
                    cnt += cookies[j]
                    mx = max(mx,cookies[j])
            cd[m] = cnt
            dp[-1][m^((1<<lc)-1)] = cnt
        
        for i in range(k-2,-1,-1):
            for m in range(1<<lc):
                for tm in range(1<<lc):
                    if (m&tm) == 0:
                        dp[i][m] = min(dp[i][m], max(cd[tm],dp[i+1][m|tm]))
        
        return dp[0][0]
            