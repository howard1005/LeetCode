class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = float('inf')
        for price in prices:
            ans = max(ans,price-mn)
            mn = min(mn,price)
        return ans