from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        td = sorted([(startTime[i],endTime[i],profit[i]) for i in range(len(startTime))])
        dp = [-1 for _ in range(len(startTime))]
        dp[-1] = td[-1][2]
        
        for i in range(len(td)-2,-1,-1):
            s,e,p = td[i]
            dp[i] = max(dp[i],dp[i+1])
            j = bisect_left(td,e,i+1,len(td),key=lambda x:x[0])
            dp[i] = max(dp[i],(dp[j] if j < len(dp) else 0)+p)
        
        return dp[0]
        