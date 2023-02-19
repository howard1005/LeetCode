from bisect import bisect_left

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        ans = 0
        
        dp = [(1,1)]
        mmx = 1
        for i in range(1,len(nums)):
            d = defaultdict(int)
            for j in range(i):
                if nums[i] > nums[j]:
                    d[dp[j][0]] += dp[j][1]
            mx = 0
            cnt = 1
            if d:
                mx = max(d)
                cnt = d[mx]
            dp.append((mx+1,cnt))
            mmx = max(mmx,mx+1)
        
        for size,cnt in dp:
            if size == mmx:
                ans += cnt

        return ans