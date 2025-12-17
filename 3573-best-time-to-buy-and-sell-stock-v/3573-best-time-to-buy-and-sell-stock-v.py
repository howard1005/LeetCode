class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        ans = 0

        sdp1 = [[-inf for _ in range(k+1)] for _ in range(len(prices))]
        sdp2 = [[-inf for _ in range(k+1)] for _ in range(len(prices))]
        dp = [[-inf for _ in range(k+1)] for _ in range(len(prices))]

        @cache
        def sub_dfs1(i,kk):
            if i >= len(prices):
                return -inf
            if sdp1[i][kk] != -inf:
                return sdp1[i][kk]
            sdp1[i][kk] = max(prices[i]+dfs(i+1,kk),sub_dfs1(i+1,kk))
            return sdp1[i][kk]

        @cache
        def sub_dfs2(i,kk):
            if i >= len(prices):
                return -inf
            if sdp2[i][kk] != -inf:
                return sdp2[i][kk]
            sdp2[i][kk] = max(-prices[i]+dfs(i+1,kk),sub_dfs2(i+1,kk))
            return sdp2[i][kk]
        
        @cache
        def dfs(i,kk):
            if i >= len(prices) or kk <= 0:
                return 0
            if dp[i][kk] != -inf:
                return dp[i][kk]

            ret = dfs(i+1,kk)
            
            if kk > 0 and i < len(prices):
                ret = max(ret,max(-prices[i]+sub_dfs1(i+1,kk-1),prices[i]+sub_dfs2(i+1,kk-1)))
                # for j in range(i+1,len(prices)):
                #     p = abs(prices[i]-prices[j])
                #     ret = max(ret,dfs(j+1,kk-1)+p)

            dp[i][kk] = ret

            return ret
        
        # for i in range(len(prices)-1,-1,-1):
        #     print(f"{i} : {dfs(i,k)}")

        ans = dfs(0,k)

        return ans