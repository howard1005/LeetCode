class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        ans = 0

        cum = 0
        for p,s in zip(prices,strategy):
            cum += p*s

        ans = cum

        a,b,c = 0,k//2,k
        for i in range(b):
            cum -= prices[i]*strategy[i]
        for i in range(b,k):
            cum -= prices[i]*strategy[i]
            cum += prices[i]

        ans = max(ans,cum)

        while c < len(prices):
            
            cum += prices[a]*strategy[a]
            a += 1

            cum -= prices[b]
            b += 1

            cum -= prices[c]*strategy[c]
            cum += prices[c]
            c += 1

            ans = max(ans,cum)

            
        return ans