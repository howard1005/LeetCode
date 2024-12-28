class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        l = [n for n in nums]
        for i in range(1,len(l)):
            l[i] += l[i-1]

        def get_sum(i):
            if i+k-1 >= len(l):
                return 0
            return l[i+k-1]-(l[i-1] if i>0 else 0)

        dp = [[(-1,tuple()) for _ in range(len(nums))] for _ in range(3)]

        for i in range(2,-1,-1):
            for j in range(len(nums)-1,-1,-1):
                if i == 2:
                    v,t = dp[i][j+1] if j+1<len(nums) else (-1,tuple())
                    cum = get_sum(j)
                    if v <= cum:
                        dp[i][j] = (cum,(j,))
                    else:
                        dp[i][j] = dp[i][j+1] if j+1<len(nums) else (-1,tuple())
                else:
                    v,t = dp[i][j+1] if j+1<len(nums) else (-1,tuple())
                    v2,t2 = dp[i+1][j+k] if j+k<len(nums) else (-1,tuple())
                    cum = get_sum(j)
                    if v <= cum+v2:
                        if len(t2)>0:
                            dp[i][j] = (cum+v2, (j,)+t2)
                    else:
                        dp[i][j] = dp[i][j+1] if j+1<len(nums) else (-1,tuple())

        # for r in dp:
        #     print(r)

        return dp[0][0][1]