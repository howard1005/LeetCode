class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        l = [(i,v) for i,v in enumerate(arr)]
        l.sort(key=lambda x:x[1])
        # print(l)

        dp = [0 for _ in range(len(l))]

        for i,v in l:
            dp[i] = 1
            j = i-1
            while j>=0 and j>=i-d and arr[j]<v:
                dp[i] = max(dp[i],1+dp[j]) 
                j -= 1
            j = i+1
            while j<len(l) and j<=i+d and arr[j]<v:
                dp[i] = max(dp[i],1+dp[j])
                j += 1

        # print(dp)

        ans = max(dp)

        return ans