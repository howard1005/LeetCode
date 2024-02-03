class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for _ in range(len(arr))]
        
        for i in range(len(arr)-1,-1,-1):
            mx = 0
            for j in range(i,min(i+k,len(arr))):
                mx = max(mx,arr[j])
                dp[i] = max(dp[i],(dp[j+1] if j+1<len(arr) else 0)+mx*(j-i+1))
        
        return dp[0]