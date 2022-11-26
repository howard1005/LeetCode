class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        td = sorted([(startTime[i],endTime[i],profit[i]) for i in range(len(startTime))])
        dp = [-1 for _ in range(len(startTime))]
        def dfs(i,t):
            if len(startTime)==i:
                return 0
            s,e,p = td[i]
            ret = 0
            if s<t:
                ret = dfs(i+1,t)
            else:
                if dp[i] != -1:
                    return dp[i]
                dp[i] = 0
                ret = max(ret,dfs(i+1,t))
                ret = max(ret,dfs(i+1,e)+p)
                dp[i] = ret
            return ret
        return dfs(0,0)
        