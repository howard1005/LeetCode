class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 0

        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        l = list(d.keys())
        l.sort(reverse=True)
        
        dp = defaultdict(int)
        
        for n in l:
            if n == 1:
                cnt = d[n]
                if cnt&1:
                    ans = max(ans,cnt)
                else:
                    ans = max(ans,cnt-1)
                continue
            dp[n] = 1
            if d[n] > 1:
                dp[n] = 1+dp[n*n]
            ans = max(ans,dp[n]*2-1)
        # print(dp)

        return ans