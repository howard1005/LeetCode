class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        dp = [0 for _ in range(len(s))]
        dp[-1] = 1

        for i in range(len(dp)-2,-1,-1):
            if i != 0:
                dp[i] += dp[i+1]
            if s[i] == '1':
                continue
            a,b = i+minJump,min(i+maxJump,len(dp)-1)
            if a < len(dp):
                dp[i] += dp[a]-(dp[b+1] if b+1<len(dp) else 0)
            
        # print(dp)
        
        ans = dp[0] > 0

        return ans
            
