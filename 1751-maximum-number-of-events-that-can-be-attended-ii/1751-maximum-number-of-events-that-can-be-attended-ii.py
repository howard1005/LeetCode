from bisect import bisect_right

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort()
        
        dp = [[0 for _ in range(k+1)] for _ in range(len(events))]
        
        for j in range(1,k+1):
            dp[-1][j] = events[-1][2]
        
        for i in range(len(events)-2,-1,-1):
            for j in range(k+1):
                dp[i][j] = max(dp[i][j], dp[i+1][j])
                if j:
                    ii = bisect_right(events, events[i][1], i+1, len(events), key=lambda x:x[0])
                    dp[i][j] = max(dp[i][j], (dp[ii][j-1] if ii < len(events) else 0) + events[i][2])

        return dp[0][k]