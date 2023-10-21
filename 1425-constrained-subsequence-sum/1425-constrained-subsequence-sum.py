from heapq import heappush,heappop

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in range(len(nums))]
        
        hq = []
        
        for i in range(len(nums)-1,-1,-1):
            j = i + k
            while hq and hq[0][1] > j:
                heappop(hq)
            
            dp[i] = nums[i]
            if hq and -hq[0][0] > 0:
                dp[i] += -hq[0][0]
            
            heappush(hq,(-dp[i],i))
        
        
        return max(dp)
            