class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ans = 0
        
        l = list(zip(scores,ages))
        l.sort()
        l.reverse()
        
        dp = [0 for _ in range(len(l))]
        dp[-1] = l[-1][0]
        for i in range(len(l)-2,-1,-1):
            mx = 0
            for j in range(i+1,len(l)):
                if l[j][1] <= l[i][1]:
                    mx = max(mx,dp[j])
            dp[i] = l[i][0]+mx
        
        return max(dp)