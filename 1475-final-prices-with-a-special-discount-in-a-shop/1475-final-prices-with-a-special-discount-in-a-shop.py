class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []

        for i in range(len(prices)):
            t = 0
            for j in range(i+1,len(prices)):
                if prices[i] >= prices[j]:
                    t = prices[j]
                    break
            ans.append(prices[i]-t)

        return ans